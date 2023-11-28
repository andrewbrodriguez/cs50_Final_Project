import json
import os
import openai
import requests

def create_image(prompt):
    # Open and read the API key from secrets.json
    with open('secrets.json') as f:
        data = json.load(f)

    key = data["dalle"]
    openai.api_key = key
    output_directory = "images"

    promptNumber = prompt[0]
    prompt = prompt[1:]

    description = prompt
    style = "a renaissance painting"

    response = openai.Image.create(
        prompt=description + " in the style of " + style,
        n=1,
        size="512x512"
    )

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Download and save the images
    data = response['data']
    link = data[0]
    link = link["url"]
    image_data = requests.get(link).content
    image_path = os.path.join(output_directory, f'image_{promptNumber}.png')

    with open(image_path, 'wb') as image_file:
        image_file.write(image_data)

    return response

