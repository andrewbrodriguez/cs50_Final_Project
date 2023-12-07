from image_gen import create_img
from prompt_gen import make_prompts
import json
from math import floor

def ingest(text):
    
    sentences = 0

    for c in text:
        if c == "." or c == "!" or c == "?":
            sentences +=1


    block_size = int(sentences/6)


    counter = 0
    block = ""
    blocks = []
    for c in text:
        block += c
        if c == "." or c == "!" or c == "?":
            counter += 1
        if counter > block_size:
            blocks.append(block)
            block = ""
            counter = 0

    blocks.append(block)


    json_filename = 'blocks.json'
    
    with open(json_filename, 'w') as json_file:
        json.dump(blocks, json_file, indent=2)
    return blocks


def run(story):
    ingested = ingest(story)

    prompts = make_prompts(ingested)

    print(len(prompts))
    
    counter = 0
    for prompt in prompts:
        print("Image " + str(counter ) + " started!")
        create_img(prompt)
        counter+=1
