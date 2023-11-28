import json
import openai

def create_prompt():

	f = open('secrets.json')

	data = json.load(f)

	key = data["gpt"]

	file = open("sample.txt", "r")
	content = file.read()


	openai.api_key = key
	messages = [ {"role": "system", "content": 
				"Describe the sceneary for the following story, such that the story could be painted, in less than 2 sentences. The story goes as follows: " + content} ] 
	while True: 
		message = input("User : ") 
		if message: 
			messages.append( 
				{"role": "user", "content": message}, 
			) 
			chat = openai.ChatCompletion.create( 
				model="gpt-3.5-turbo", messages=messages 
			) 
		reply = chat.choices[0].message.content 
		print(f"ChatGPT: {reply}") 
		messages.append({"role": "assistant", "content": reply}) 
