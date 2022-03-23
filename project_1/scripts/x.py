import yfinance
from plotly import graph_objects

# get the data in a dataframe object
ticker = yfinance.Ticker("AAPL")
dataframe = ticker.history("3y")

yesterday_high = dataframe["High"]["2022-03-23"]

print(dataframe)
print(yesterday_high)

# diagram = graph_objects.Figure(
#     graph_objects.Candlestick(
#         x=dataframe.index,
#         low=dataframe["Low"],
#         high=dataframe["High"],
#         open=dataframe["Open"],
#         close=dataframe["Close"],
#     )
# )
#
# diagram.show()
