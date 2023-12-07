# BAM's AI Picture Book

Our program converts an inputted story into a series of images using the DALL·E API. For a quick tour of our project, please view this video!

## Installation

Clone the repository - where does the project currently live? @Andrew

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages: cs50, flask, flask_session, werkzeug.security, functools, openai, requests, and json. These imports are also in requirements.txt, so we can install them all with the command below.

```bash
pip install -r requirements.txt
```

You should also be aware that while attempting to run our code on different group members' computers, we encountered a strange error: 

```bash
AttributeError: module 'hashlib' has no attribute 'scrypt'
```

The CS50 staff was not able to figure out the specifics of this error, but we fixed it by uninstalling python in our codespaces and reinstalling pyenv via Homebrew.

## Quickstart

1. Run the project using 
```bash
flask run ??? @Andrew... making flask object? anything to do with sql?
```
2. Register with a password that has at least one number and at least one special character or log in to BAM’s AI Picture Book.
3. Navigate to “Input.”
4. You can test our code using the textbox. There are three stories in the file samples.txt for you to test, or create your own! Feel free to use ChatGPT for help creating stories. Your story must be between 100 and 5000 characters.
5. To view your space on the user stats leaderboard, navigate to “User Stats.”

## Authors

This project was designed and written by Andrew Rodriguez, Ben Ford, and Maddie Stearns.
