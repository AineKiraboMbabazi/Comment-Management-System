import datetime


class Comment:
    def __init__(self, text, username):
        self.text = text
        self.username = username
        self.timestamp = datetime.datetime.now()

    def text(self):
        return self.text

    def username(self):
        return self.username