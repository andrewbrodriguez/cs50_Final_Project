# BAM's AI Picture Book

Our program converts an inputted story into a set of 10 images using the DALL·E and Chat GPT API. For a quick tour of our project, please view this video!

## Installation

Clone the repository from here: https://github.com/andrewbrodriguez/cs50_Final_Project 

Make sure to grab the secrets.json file from an email from Ben, Maddie, or Andrew. This file is not in our GitHub and was added
to our gitIgnore because pushing an OpenAI API key freezes that key. If you do not have this file in your email just shoot one of
us an email and we can send it over to you. You can reach out to us at: arodriguez@college.harvard.edu, mstearns@college.harvard.edu,
and bgford@college.harvard.edu

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages: cs50, flask, flask_session, werkzeug.security, functools, openai (notably version 0.28), requests, and json. These imports are also in requirements.txt, so we can install them all with the command below.

```bash
pip install -r requirements.txt
```

You should also be aware that while attempting to run our code on different group members' computers, we encountered a strange error: 

```bash
AttributeError: module 'hashlib' has no attribute 'scrypt'
```

The CS50 staff was not able to figure out the specifics of this error, but we fixed it by uninstalling python in our codespaces and reinstalling pyenv via Homebrew. This is likely a long winded dependency error, so apologies if you get the same error!

## Quickstart

1. Run the project by using the below command while in the code directory
```bash
flask --app app run
```
2. Register with a password that has at least one number and at least one special character or log in to BAM’s AI Picture Book.
3. Navigate to “Input.”
4. You can test our code using the textbox. There are three stories in the file samples.txt for you to test, or create your own! Feel free to use ChatGPT for help creating stories. Your story must be between 500 and 10000 characters. We would reccomend you err
on the side of a page or two for speed and simplicity sake. 
5. To view your space on the user stats leaderboard, navigate to “User Stats.”

## Authors

This project was designed and written by Andrew Rodriguez, Ben Ford, and Maddie Stearns.
