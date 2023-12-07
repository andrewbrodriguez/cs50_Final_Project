# Import our functions and json
from image_gen import create_img
from prompt_gen import make_prompts
import json

# Ingest is going to split the story into blokcs
def ingest(text):
    
    # Count up the number of sentences in the story
    sentences = 0
    # We do this by iteration
    for c in text:
        if c == "." or c == "!" or c == "?":
            sentences +=1
    # Set the block size to one fifth of the story
    block_size = int(sentences/10)

    # Create a new for loop to save each block
    counter = 0
    block = ""
    blocks = []
    for c in text:
        block += c
        if c == "." or c == "!" or c == "?":
            counter += 1
        # If we have a block add it to our blocks
        if counter > block_size:
            blocks.append(block)
            # Reset blocks and counter
            block = ""
            counter = 0

    # Append the final block
    blocks.append(block)

    # Write and save our block to a json for later purposees
    json_filename = 'blocks.json'
    with open(json_filename, 'w') as json_file:
        json.dump(blocks, json_file, indent=2)
    return blocks

# Now the main run function
def run(story):
    # Ingest the story for blocks
    ingested = ingest(story)
    # Create prompts from those blocks
    prompts = make_prompts(ingested)
    # Create images from those prompts
    for prompt in prompts:
        create_img(prompt)
