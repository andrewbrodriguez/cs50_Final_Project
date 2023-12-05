from image_gen import create_img
from prompt_gen import make_prompts
import json

def ingest(text):
    counter = 0
    block = ""
    blocks = []
    for c in text:
        block += c
        if c == "." or c == "!" or c == "?":
            counter += 1
        if counter == 3:
            print(block)
            blocks.append(block)
            block = ""
            counter = 0

    json_filename = 'blocks.json'
    
    with open(json_filename, 'w') as json_file:
        json.dump(blocks, json_file, indent=2)
    return blocks


def run(story):
    ingested = ingest(story)

    prompts = make_prompts(ingested)

    for prompt in prompts:
        create_img(prompt)
