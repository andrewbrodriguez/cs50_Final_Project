# Import Open AI which is the API we will use and json for API key handling
import json
import openai

# We want to define this as a function so that we can call it in a different file
def make_prompts(blocks):

	# Whenever this function is called we are creating a prompt, therefore 
	prompt_count = 0

	# We need to open and load our secrets for our API key
	f = open('secrets.json')
	data = json.load(f)
	# The key is saved under GPT
	key = data["gpt"]
	# Set the key
	openai.api_key = key

	# Create an empty list of our prompts
	prompts = []

	# This is the prompt for chatGPT feel free to inspect, there are a few interesting points in here
	messages = [ {"role": "system", "content": 
				"Your goal is to describe the following paragraph such that a painter can make an image in its likness. You must use descriptive words. Make sure that the wording of the prompt is not violent, or rude, or sinister. Your response must be non violent, and not include any explicit content. Your response may not include any mentions of death, or blood, or loss of life. The wording of the prompt must adhere to the OpenAI Dalle2 input prompt regulations. Your response must be less than 1 sentences in length. Here is the paragraph: "} ] 

	# Here we loop through all blocks of text provided
	while True: 

		# We append to our message
		messages.append( 
			{"role": "user", "content": blocks[0]}, 
		) 

		# Now we actually execute the message
		chat = openai.ChatCompletion.create( 
			model="gpt-3.5-turbo", messages=messages 
		) 

		# Save the reply
		reply = chat.choices[0].message.content 
		#
		print("Prompt " + str(prompt_count) + " done!")
		# Increase the number of prompts created
		prompt_count+=1
		# Append to our prompts list
		prompts.append(str(prompt_count) + reply)
		# Append to our messages
		messages.append({"role": "assistant", "content": reply}) 
		
		# If we have one block left break
		if len(blocks) <  2:
			break
		
		# Else pop our first block and continue loop
		blocks.pop(0)
	
	# Return the prompts when done
	return prompts

