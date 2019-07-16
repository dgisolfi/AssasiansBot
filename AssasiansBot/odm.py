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
        
        # create a connection
        self.couch = self.connect()
        # Get or create the db
        self.db = self.getDatabase()
        

    def connect(self):
        """ 
        """
        url = f'http://{self.user}:{self.password}@{self.host}:{self.port}/'

        print(url)
        try:
            return pycouchdb.Server(url) 
        except:
            raise ValueError('Cannot Connect to CouchDB')

       
    def getDatabase(self):
        """ 
        """
        if self.db_name in self.couch:
            return self.couch.database(self.db_name)
        else:
            return self.couch.create(self.db_name)      
    

odm = ODM()