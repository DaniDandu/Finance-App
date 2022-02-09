# this is our root file, when we execute this we will start our app
import json
from fastapi import FastAPI

app = FastAPI(
    title="Name of our app",
    # <major_version>.<minor_version>.<patch_version>
    version="0.2.0",
)
# uvicorn index:app --reload --post 7777
# uvicorn is the server which will start
# index:app, index -> the file name, app -> the FastAPI object name
# --reload -> the server will restart when we modify the code
# --post <port_number> -> select on which port to start


@app.get(
    "/health",
    summary="This will be visible at start",
    description="We can describe this API call",
    response_description="We can describe the response",
)
def health() -> dict:
    return {
        "status": "online",
        "engine": "on",
    }

list_of_items = []

@app.post("/items")
def add_new_item(request: dict):
    list_of_items.append(request)
    list_json = json.dumps(list_of_items)
    file = open("database.txt", "w")
    file.write(list_json)
    file.close()


@app.get("/items")
def get_items():
    return list_of_items


@app.on_event("startup")
def load_list_of_items():
    file = open("database.txt")
    json_items = file.read()
    file.close()
    list_of_items.append(json.loads(json_items))

