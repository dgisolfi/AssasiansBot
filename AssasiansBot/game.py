#!/usr/bin/python3
# 2019-7-16

from AssasiansBot.odm import ODM
from datetime import datetime

class Game:
    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.odm = ODM()


    def setup(self, start_date):
        """
        Creates a new instance of a game and saves it to the database

        Parameters
        ----------
        start_date : datetime - format: Oct 24 1998 1:33PM
            The datetime when the game should begin (if the format is not 
            valid the game will not be created and the user will be alerted).
        Returns
        -------
        new_game_msg : string
            The game has been setup and there are no issues
        error : string
            an error has occured while setting up a new game, the details 
            of this error will be returned to the user
        """
        new_game_msg = (
            'Welcome to Assasians, if you would like to join \n'
            'send the a message with the form:'
            f'\n@{self.bot_name} join your.email@domain.com\n '
            f'If you need any help just send: \n@{self.bot_name} help\n'
            'Once the game begins your target will be sent to the email you'
            'provided, If you do not recived an email talk Daniel.'
            'Warning: If your just being stupid you must buy him a beer.'
            f'The murder and humilation spree begins at {self.start_date}'
            'You have until then to join'
        )

        # Check if the start_date is a valid datetime otherwise reject
        try:
            # format : Jun 1 2005  1:33PM
            datetime.strptime(start_date, '%b %d %Y %I:%M%p')
        except:
            return (
                'Error: the given datetime is not in the valid format.'
                'Please use the format: Oct 24 1998 1:33PM'
            )
       
        # Next, create a new instance of the game in the database 
        # for future reference
        
        # TODO: catch this 
        game = self.odm.createGame(start_date)
        return new_game_msg

    def help(self):
        """
        Returns a list of all supported commands

        Returns
        -------
        help_msg : string
            a list of all supported commands and their parameters
        """

        help_msg = (
            'Here is a list of the possible commands:\n'
            '\tnew game <start_time>\n'
            '\thelp\n'
            '\trules\n'
            '\tjoin <email_address>\n'
            '\tremaining players\n'
            '\tconfirm kill\n'
        )
        return help_msg

    def rules(self):
        """
        Returns a list of game rules

        Returns
        -------
        rules_msg : string
            a list of all the rules of assasians
        """
        rules_msg = (
            ''
        )
        return rules_msg

    def join(self, user_id, name, email):
        """
        Adds a user to a game

        Parameters
        ----------
        user_id : integer
            the unique user ID assigned by groupme
        email : string
            the email address to reach a user at

        Returns
        -------
        """
        # TODO: Catch the create issues

        # TODO: If success send a test email
        player = self.odm.createPlayer(user_id, name, email)

        game = self.odm.getGame()
        game = game['remaining_players'].append(user_id)
        self.odm.updateGame(game)

       

        return (
            f'{name} has been added to the game. '
            'Test email sent. Happy Hunting.'
        )

    def start(self):
        pass

    def remainingPlayers(self):
        pass

    def end(self):
        pass

    def confirmKill(self, user_id):
        pass