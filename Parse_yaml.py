import yaml
from yaml import load

data = open("YAML.yaml").read()

yaml_data = load(data, Loader=yaml.FullLoader)

#print(yaml_data)

print("====== SPINE ========")
for spine in yaml_data["spine"]:
    print("Switch is: {} " .format(spine["switch"]))
    print("Switch type is: {} ".format(spine["type"]))
    print("Switch hostaname is: {} ".format(spine["hostname"]))

print("====== LEAF =========")
for leaf in yaml_data["leaf"]:
    print("Switch is: {} ".format(leaf["switch"]))
    print("Switch type is: {} ".format(leaf["type"]))
    print("Switch hostaname is: {} ".format(leaf["hostname"]))
