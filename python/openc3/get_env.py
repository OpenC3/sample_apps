import os

class GetEnv:
    def __init__(self):
        self.stdout = ''
    
    def run(self):
        if os.environ['ENV'] == 'prod':
            self.stdout = 'Production environment'
        else:
            self.stdout = 'Development environment'
    