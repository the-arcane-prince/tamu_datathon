import json

json_f = open("data_green.json", "r")
json_data = json.load(json_f)
json_f.close()

print(json_data)