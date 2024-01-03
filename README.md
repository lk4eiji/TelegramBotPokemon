# POKEMON BOT TELEGRAM

This repository contains the code for creating a Telegram bot using the Python Telebot library. The purpose of this application is to generate a bot that, when queried about the name of any Pokémon, will send you the Pokémon's image along with its statistics.


## Configuration and Installation
1. Clone this repository.
2. Install the dependencies by running `pip install -r requirements.txt`.
3. Create a bot on Telegram using BotFather and obtain your token.
4. Replace 'YOUR_TOKEN_HERE' in 'pokebot.py' with your obtained token.
5. Execute the app with `python pokebot.py`.


## Functionalities
- The bot responds to the following commands: `/start`, `/help`, and `/search`.
- The bot provides information when someone tries to send any message that doesn't correspond to the commands.

## Suggestions 
Remember, if you're going to upload the app, I recommend using an env var instead of a 'TOKEN' variable to enhance your app's security.