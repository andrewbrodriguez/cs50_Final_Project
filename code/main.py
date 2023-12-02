from image_gen import create_image
from prompt_gen import create_prompts

def ingest(text):
    counter = 0
    block = ""
    blocks = []
    for c in text:
        block += c
        if c == "." or c == "!" or c == "?":
        #     counter += 1
        # if counter == 10:
            print("bonk")
            print(block)
            blocks.append(block)
            block = ""
            # counter = 0
    return blocks


def run(story):
    print("story")
    print(story)
    ingested = ingest(story)

    prompts = create_prompts(ingested)

    text_prompts = ""

    print(prompts)
    print("RIGHT HERE")
    for prompt in prompts:
        print("BEANNNNNN")
        print(prompt)
        text_prompts += prompt 
        text_prompts += "\n\n"

    with open('prompts.txt', 'w') as f:
        f.write(text_prompts)


    for prompt in prompts:
        create_image(prompt)

