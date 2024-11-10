import json

jr = open("data.json", "r")

gw = open("data_green.json", "w")
yw = open("data_yellow.json", "w")
bw = open("data_blue.json", "w")
pw = open("data_purple.json", "w")

json_data = json.load(jr)

gjson = []
yjson = []
bjson = []
pjson = []

for game in json_data:
    for part in game:
        color = part['color']
        new_part = {
            'category': part['category'],
            'words': part['words'],
        }
        match color:
            case 'green':
                gjson.append(new_part)
            case 'yellow':
                yjson.append(new_part)
            case 'blue':
                bjson.append(new_part)
            case 'purple':
                pjson.append(new_part)
                
json.dump(gjson, gw)
json.dump(yjson, yw)
json.dump(bjson, bw)
json.dump(pjson, pw)

gw.close()
yw.close()
bw.close()
pw.close()
jr.close()