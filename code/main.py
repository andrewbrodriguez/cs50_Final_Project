from image_gen import create_img
from prompt_gen import make_prompts

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
    return blocks


def run(story):
    ingested = ingest(story)

    prompts = make_prompts(ingested)

    text_prompts = ""

    for prompt in prompts:
        text_prompts += prompt 
        text_prompts += "\n\n"

    with open('prompts.txt', 'w') as f:
        f.write(text_prompts)


    for prompt in prompts:
        create_img(prompt)
