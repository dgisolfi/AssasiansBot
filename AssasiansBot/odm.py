#!/usr/bin/python3
# Author: Tyler Rimaldi

import os
import pycouchdb
import requests
import json

"""
Object Document Mapper
"""

class ODM:
    def __init__(self):
        # Database Information
        self.user = os.getenv('COUCHDB_USER', None)
        self.password = os.getenv('COUCHDB_PASSWORD', None)
        self.host = os.getenv('COUCHDB_HOST', None)
        self.port = 5984#os.getenv('COUCHDB_PORT', 5984)
        self.db_name = os.getenv('COUCHDB_DB', None)
        self.conn_url = (
            f'http://{self.user}:{self.password}@{self.host}:{self.port}'
        )
        
        # create a connection
        self.couch = self._connect()
        # Get or create the db
        self.db = self._getDatabase()
        

    def _connect(self):
        """ 
        """
        
        try:
            return pycouchdb.Server(self.conn_url) 
        except:
            raise ValueError('Cannot Connect to CouchDB')

    def _getDatabase(self):
        """ 
        """
        if self.db_name in self.couch:
            return self.couch.database(self.db_name)
        else:
            return self.couch.create(self.db_name)  

    ''' Basic interactions from pycouchdb '''
    def _get(self, _id):
        return self.db.get(_id)

    def _create(self, obj):
        return self.db.save(obj)

    def _delete(self, _id):
        return self.db.delete(_id)
    
    ''' Additional features '''

    def _find(self, query):
        response = requests.post(f'{self.conn_url}/{self.db_name}/_find', json=query)
        if response.status_code is not 200:
            raise ValueError('Error while running find on given selector')
        else:
            return response.json()['docs']

    def _update(self, _id, json):
        doc = self._get(_id)
        json['_rev'] = doc['_rev']

        response = requests.put(
            f'{self.conn_url}/{self.db_name}/{_id}', 
            json=json
        )
        if response.status_code is not 201:
            raise ValueError('Error while updating document')
        else:
            return response.json()

    ''' Object Logic '''

    def createGame(self, start_date):
        game = {
            'status': 'active',
            'start_date': start_date,
            'remaining_players': [],
            'killed_players': [],
            'winner':''
        }
        return self._create(game)

    def getGame(self):
        query = {
            'selector': {
                'status': {
                    '$eq': 'active'
                }
            }
        }
        return self._find(query)
    
    def updateGame(self, json):
        game = self.getGame()
        self._update(game[0]['_id'], json)
    
    def createPlayer(self, user_id, name, email):
        player = {
            'user_id':user_id,
            'name': name,
            'email': email,
            'status': 'alive',
            'target': ''
        }
        return self._create(player)

    def getPlayer(self, user_id):
        query = {
            'selector': {
                'user_id': {
                    '$eq': user_id
                }
            }
        }
        return self._find(query)
    
    def updatePlayer(self, user_id, json):
        player = self.getPlayer(user_id)
        self._update(player[0]['_id'], json)
    

odm = ODM()
odm.updatePlayer(2343, {
  "_id": "3351ffb1e821403f9aeacf8e79683a3b",
  "user_id": 2343,
  "name": "daniel",
  "email": "Daniel@",
  "status": "dead",
  "target": ""
})
print(odm.getPlayer(2343))