# Import packages needed
import json
import os
import openai 
import requests
import shutil


# Again we use a function so we can import this into another file later
def create_img(prompt):
    # We track the number of prompts and the number 
    promptNumber = prompt[0]
    prompt = prompt[1:]

    # We use a try except in the case that this fails due to a violent image or billing limit
    try:    
        # Make sure the prompt is the right length
        prompt = prompt[0:399]
        # Open and read the API key from secrets.json
        with open('secrets.json') as f:
            data = json.load(f)
        key = data["dalle"]

        # Set up open AI
        openai.api_key = key

        # Set our output directory
        output_directory = "static/images"

        # Set our description and style 
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

        # Unwrap URL from response
        data = response['data']
        link = data[0]
        link = link["url"]
        # Download and save images
        image_data = requests.get(link).content
        image_path = os.path.join(f'static/images/{promptNumber}.png')

        # Save it locally
        with open(image_path, 'wb') as image_file:
            image_file.write(image_data)
        
        return "Completed!"
    
    except Exception as e:
        # If an error occurs, copy the error image in its place
        shutil.copy("static/er.png", (f'static/images/{promptNumber}.png'))
        return "Completed with an error"
    


