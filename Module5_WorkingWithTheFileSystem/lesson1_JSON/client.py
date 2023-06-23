import json

client_info = {}


def load():
    global client_info
    with open("client_info.json", "r", encoding="UTF-8") as json_fiel:
        client_info = json.load(json_fiel)


def save():
    global client_info
    with open("client_info.json", "w", encoding="UTF-8") as json_fiel:
        json.dump(client_info, json_fiel)
