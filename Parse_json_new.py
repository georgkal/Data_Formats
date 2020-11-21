import json

data = open("JSON.json").read()

json_data = json.loads(data)

print(json_data)

print("====== SPINE ========")
for spine in json_data["spine"]:
    print("Switch is: {} " .format(spine["switch"]))
    print("Switch type is: {} ".format(spine["type"]))
    print("Switch hostaname is: {} ".format(spine["hostname"]))

print("====== LEAF =========")
for leaf in json_data["leaf"]:
    print("Switch is: {} ".format(leaf["switch"]))
    print("Switch type is: {} ".format(leaf["type"]))
    print("Switch hostaname is: {} ".format(leaf["hostname"]))
