import json

# Открыть на чтение фаил client_info.json как json файл
with open("client_info.json", "r", encoding="utf-8") as json_file:
    test = json.load(json_file)

# JSON в питоне хранится как словарь

test["name"] = "Андрей"

test["accounts"].append(
    {
        "name": "На море",
        "system": "MIR Classic",
        "number": "7777 0000 7777 9999",
        "type": "дебетовая",
        "balance": 30459,
        "validity period": "11/2023"
    }
)

print(test)

#открыть файл на запись

with open("client_info_test.json", "w", encoding="utf-8") as outfile:
    json.dump(test, outfile)

#Записать test в открытый файл outfile