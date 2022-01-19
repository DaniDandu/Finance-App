import requests

url = "http://127.0.0.1:7776"
requests.post(url, json={"name": "Game of Thrones", "pages": 600, "author": "Geroge Martin"})
requests.post(url, json={"name": "Amintiri din copilarie", "pages": 200, "author": "Ion Creanga"})
requests.post(url, json={"name": "2052", "pages": 473, "author": "Jørgen Randers"})

# requests.delete(url, json={"name": "Amintiri din copilarie"})



requests.put(url, json={"name": "2052", "pages": 90})
