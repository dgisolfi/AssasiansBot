#!/usr/bin/python3
# 2019-7-16

import os
import markdown
from AssasiansBot.bot import Bot
from flask import Flask, request

# Create instance of flask
server = Flask(__name__)
server.config['JSON_SORT_KEYS'] = False

bot_name = os.getenv('BOT_NAME', None)
bot_id = os.getenv('BOT_ID', None)
group_id = os.getenv('GROUP_ID', None)
api_token = os.getenv('API_TOKEN', None)

# setup bot
bot = Bot(bot_name, bot_id, group_id, api_token)

@server.route('/', methods=['GET'])
def index():
    try:
        markdown_file = open('README.md', 'r')
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content), 200
    except:
        return 'Project Documentation Not found', 404
        
@server.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    if data is not None:
        if bot.checkForMention(data['text']):
            msg = bot.removeMention(data['text'])
            cmd = bot.validCmd(msg)
            if cmd is not None:
                response = bot.run(data, cmd, msg)
                print(response)
                return 'OK', 200
            else:
                response = (
                    f'"{msg}" is not a valid command. '
                    'Run "help" for a list of valid commands'
                )
                return 'not a valid command', 400
           
            # bot.sendMessage(response)
        else:
            return 'Bot Not Mentioned', 404
    else:
        return 'No Message Provided', 404
