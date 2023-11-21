import json

f = open('secrets.json')

data = json.load(f)

key = data["dalle"]


