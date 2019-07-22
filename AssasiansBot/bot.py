#!/usr/bin/python3
# 2019-7-16

import re
import requests
from AssasiansBot.game import Game
from AssasiansBot.commands import cmds


class Bot:
    def __init__(self, bot_name, bot_id, group_id, api_token):
        self.bot_id = bot_id
        # This is the user ID of the person who should be "mocked"
        self.group_id = group_id
        self.api_token = api_token
        self.api_base_url = 'https://api.groupme.com/v3'
        self.api_session = requests.session()
        self.name = bot_name
       
    def sendMessage(self, msg):
        """Send a message from the bot to its assigned group.
        Parameters
        ----------
        msg : string 
            message to be sent to group
        Returns
        -------
        response : response
            the response object returned by the API call
        """
        # set parameters for post request
        params = {
            'bot_id': self.bot_id,
            'text': msg
        }
        # send the request to the api and get the results in the response var
        response = self.api_session.post(
            f'{self.api_base_url}/bots/post', 
            params=params
        )
        return response
    
    def checkForMention(self, msg):
        """Checks the recent messages of the bots group for instances of its name
        Parameters
        ----------
        msg : string
            message sent in group chat
        Returns
        -------
        boolean 
            a value denoting if the bot was mentioned or not
        """
        return re.match(r'.*@'+self.name+r'.*', msg)
    
    def removeMention(self, msg):
        """Checks the recent messages of the bots group for instances of its name
        Parameters
        ----------
        msg : string
            message sent in group chat
        Returns
        -------
        msg : string
            a messaged with the @bot_name removed
        """
        return re.sub(f'@{self.name}', '', msg)
    
    def validCmd(self, user_cmd):
        command = None
        for cmd in cmds.keys():
            if cmd in lower(user_cmd):
                command = cmd
            
        return command

    def run(self, packet, cmd, msg):
        game = Game(self.name)
        msg = lower(msg).replace(cmd, '')
        parameters = msg.split(' ')
        if cmd in ['join']:
            parameters.append(packet['user_id'])
            parameters.append(packet['name'])


        return eval(f'game.{cmd}("{*parameters}")')