#!/usr/bin/python3
# 2019-7-16

class Game:
    def __init__(self, start_date, bot_name):
        self.start_date = start_date
        self.bot_name = bot_name

    def setup(self):
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

        return new_game_msg

    def help(self, cmd):
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
        rules_msg = (
            ''
        )
        return rules_msg

    def join(self, user_id, email):
        pass

    def start(self):
        pass

    def remainingPlayers(self):
        pass

    def end(self):
        pass

    def confirmKill(self, user_id):
        pass