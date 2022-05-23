# this is our root file, when we execute this we will start our app
# webpage for fastapi framework https://fastapi.tiangolo.com/tutorial/,
# also https://realpython.com/fastapi-python-web-apis/

# uvicorn index:app --reload --port 7777
# uvicorn is the server which will start
# index:app, index -> the file name, app -> the FastAPI object name
# --reload -> the server will restart when we modify the code
# --port <port_number> -> select on which port to start


from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_utils.tasks import repeat_every
import yfinance
import logging

from stock.stock_repo import StockRepository
from configuration.config import Configuration
from database.stock_file_persistance import StockFileStockPersistance
from database.stock_sql_persistance import StockSqlPersistance
from exceptions import StockNotFound
from exceptions import StockExists
from exceptions import StockDeleted
from api.stocks import stocks_router
from api.health import health_router
from api.diagrams import diagrams_router

app = FastAPI(
    title="StockIt",
    # <major_version>.<minor_version>.<patch_version>
    version="1.0.0",
    description="Store your information about stocks in a database. "
                "With StockIt you can add, find or delete an stock. In addition you can make a diagram with the price evolution.",
)
app.include_router(stocks_router)
app.include_router(health_router)
app.include_router(diagrams_router)

conf = Configuration()
if conf.get_db_type() == "file":
    persistance = StockFileStockPersistance(conf.get_db_path())
if conf.get_db_type() == "sql":
    persistance = StockSqlPersistance(conf.get_db_path())
StockRepository.persistance = persistance
stock_repo = StockRepository()

logging.basicConfig(filename="finance.log", encoding="utf-8", level=logging.DEBUG)
logging.info("Starting the finance app ...")


@app.on_event("startup")
def load_list_of_items():
    logging.info("Loading stocks from database ...")
    stock_repo.load()
    logging.info("Successfully loaded stocks from database.")


@app.on_event("startup")
@repeat_every(seconds=5 * 60, wait_first=True)  # every 5 seconds we run this function
def update_prices():
    # get all stocks
    # get price (yfinance)
    # stock set price
    if not stock_repo.stocks:
        logging.warning("Stocks not loaded yet!")
        return
    tickers = stock_repo.stocks.keys()
    logging.info("Updating prices ...")
    for a_ticker in tickers:
        yf_ticker = yfinance.Ticker(a_ticker)
        price = yf_ticker.info["currentPrice"]
        stock_repo.stocks[a_ticker].set_price(price)


@app.exception_handler(StockNotFound)
def handle_stock_not_found(exception, request):
    return JSONResponse(content="The stock you requested was not saved in our app!", status_code=404)


@app.exception_handler(StockExists)
def handle_stock_exists(exception, request):
    return JSONResponse(content="The stock you requested is already stored in the database. Try another one!", status_code=409)


@app.exception_handler(StockDeleted)
def handle_stock_deleted(exception, request):
    return JSONResponse(content="This stock has already been deleted from the database or has not been stored.", status_code=404)
