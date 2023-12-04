import json
import os
import openai 
#import OpenAI

#client = OpenAI()
import requests

def create_image(prompt):
    # Open and read the API key from secrets.json
    with open('secrets.json') as f:
        data = json.load(f)

    key = data["dalle"]
    
    output_directory = "images"

    promptNumber = prompt[0]
    prompt = prompt[1:]

    description = prompt
    style = "a high fantasy painting"

    response = client.images.generate(prompt=description + " in the style of " + style,
    n=1,
    size="512x512")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Download and save the images
    # data = response['data']
    # link = data[0]
    # link = link["url"]
    link = response.data[0].url
    image_data = requests.get(link).content
    image_path = os.path.join(output_directory, f'image_{promptNumber}.png')

    with open(image_path, 'wb') as image_file:
        image_file.write(image_data)

    return response


def create_img(prompt):

    try:

        prompt = prompt[0:399]
        # Open and read the API key from secrets.json
        with open('secrets.json') as f:
            data = json.load(f)

        key = data["dalle"]
        openai.api_key = key
        output_directory = "images"

        promptNumber = prompt[0]
        prompt = prompt[1:]

        description = prompt
        style = "a high fantasy painting"
        
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
    
    except Exception as e:
        # If an error occurs, return an error message or handle it as needed
        return {"error": str(e)}


print(create_img("a tree"))
