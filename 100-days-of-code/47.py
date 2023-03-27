### file handling for json files ###
import json


with open("data.json", "r") as f:
    data = json.load(f)

data["person"]["name"] = "Adam"
data["person"]["age"] = 21

data["person"]["hobbies"] = ["reading", "running"]
json_string = json.dumps(data, indent=4)

with open("data.json", "w") as f:
    f.write(json_string)