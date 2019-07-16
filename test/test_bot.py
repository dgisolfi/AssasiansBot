#!/usr/bin/python3
# 2019-7-16

from AssasiansBot import Bot
import pytest
import json
import os

class TestAssasiansBot:
    bot_id = os.getenv('BOT_ID', None)
    group_id = os.getenv('GROUP_ID', None)
    api_token = os.getenv('API_TOKEN', None)

    # TODO: tests