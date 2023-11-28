import json
import openai

def create_prompts(blocks):

	prompt_count = 0

	f = open('secrets.json')
	data = json.load(f)
	key = data["gpt"]
	openai.api_key = key

	prompts = []

	messages = [ {"role": "system", "content": 
				"Describe the sceneary for the following paragraph, such that the story could be painted, in less than 2 sentences. Here is the paragraph: "} ] 

	while True: 

		messages.append( 
			{"role": "user", "content": blocks[0]}, 
		) 
		chat = openai.ChatCompletion.create( 
			model="gpt-3.5-turbo", messages=messages 
		) 
		reply = chat.choices[0].message.content 
		prompt_count+=1
		prompts.append(str(prompt_count) + reply)
		messages.append({"role": "assistant", "content": reply}) 
		
		if len(blocks) <  2:
			break

		blocks.pop(0)
		print("Prompt " + str(prompt_count) + " done!")
	

	return prompts