import json

f = open('secrets.json')

data = json.load(f)

key = data["dalle"]


import openai

PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"

openai.api_key = key 

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
)

print(response["data"][0]["url"])