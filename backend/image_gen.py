import json
import openai

import os
import openai

def create_image():
    f = open('secrets.json')

    data = json.load(f)

    key = data["dalle"]
    openai.api_key = key

    description = "The sceneary for the story 'Little Red Riding Hood' would depict a quaint village nestled among rolling hills, with a path leading to a dense and enchanting wood. Sunlight filters through the trees, casting dancing sunbeams on a carpet of colorful wildflowers. Three large oak trees stand tall near a cozy cottage where Little Red Riding Hood's grandmother resides. The atmosphere is both peaceful and mysterious, creating an idyllic yet foreboding setting for the classic tale."
    style = "a rennisance painting"

    response = openai.Image.create(
        prompt = description + " in the style of " + style,
        n = 1,
        size = "512x512"
    )
    return(response)
 
