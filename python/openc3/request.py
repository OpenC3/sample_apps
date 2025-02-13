import os
import json
import requests

class Request:
    def __init__(self):
        self.total = 0
        self.user_ids = []
    
    def run(self):
        # Make a get request to 'https://jsonplaceholder.typicode.com/posts'
        # which will return a json encoded list of posts.
        # Parse the json and store the total number of posts and the unique user ids.
        pass