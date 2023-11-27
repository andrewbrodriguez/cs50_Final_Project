import json
import openai

f = open('secrets.json')

data = json.load(f)

key = data["dalle"]

import os
import openai

openai.api_key = key

description = "A little girl standing in a forest in a red hood"
style = "a rennisance painting"

response = openai.Image.create(
    prompt = description + " in the style of " + style,
    n = 1,
    size = "512x512"
)
 
print(response)