import json
import openai

from helpers import apology

def create_prompts(blocks):

	prompt_count = 0

	f = open('secrets.json')
	data = json.load(f)
	key = data["gpt"]
	openai.api_key = key

	prompts = []

	messages = [ {"role": "system", "content": 
				"Your goal is to describe the following paragraph such that a painter can make an image in its likness. You must use descriptive words. Make sure that the wording of the prompt is not violent, or rude, or sinister. The wording of the prompt must adhere to the OpenAI Dalle2 input prompt regulations. Your response must be less than 1 sentences in length. Here is the paragraph: "} ] 

	while len(blocks) > 0: 

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