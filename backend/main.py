from image_gen import create_image
from prompt_gen import create_prompts

text = "hello world. this is me! how are you. right here. another one lol. hello world. this is me! how are you. right here. another one lol."

file = open("sample.txt", "r")
content = file.read()

def ingest(text):
    counter = 0
    block = ""
    blocks = []
    for c in text:
        block += c
        if c == "." or c == "!" or c == "?":
            counter += 1
        if counter > 10:
            blocks.append(block)
            block = ""
            counter = 0
    return blocks

ingested = ingest(content)

prompts = create_prompts(ingested)

for prompt in prompts:
    create_image(prompt)


#print(create_image())