# Error handling
import json
import os
import openai 
import requests
import shutil



def create_img(prompt):
    promptNumber = prompt[0]
    prompt = prompt[1:]

    try:
        prompt = prompt[0:399]
        # Open and read the API key from secrets.json
        with open('secrets.json') as f:
            data = json.load(f)

        key = data["dalle"]
        openai.api_key = key
        output_directory = "static/images"



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
        image_path = os.path.join(f'static/images/image_{promptNumber}.png')


        with open(image_path, 'wb') as image_file:
            image_file.write(image_data)
            
        print("image completed")
        return response
    
    except Exception as e:
        # If an error occurs, return an error message or handle it as needed
        shutil.copy("static/er.png", (f'static/images/image_{promptNumber}.png'))
        print("THREW AN ERROR")
        return {"error": str(e)}
    


