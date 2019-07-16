#!/usr/bin/python3
# 2019-7-16

import re
import requests

class Bot:
    def __init__(self, bot_id, group_id, api_token):
        self.bot_id = bot_id
        # This is the user ID of the person who should be "mocked"
        self.group_id = group_id
        self.api_token = api_token
        self.api_base_url = 'https://api.groupme.com/v3'
        self.api_session = requests.session()

       
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
    