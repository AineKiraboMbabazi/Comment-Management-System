import datetime
from database import  comments

class Comment:
    def __init__(self, text, username):
        self.id = len(comments) + 1
        self.text = text
        self.username = username
        self.timestamp = datetime.datetime.now()

    def text(self):
        return self.text

    def username(self):
        return self.username