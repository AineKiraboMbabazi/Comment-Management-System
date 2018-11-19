from database import users, comments
from Comment import Comment


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def signup(self, user):
        users.append(user)
        print("User succefully signed up")

    def login(self):
        for user in users:
            if user.username == self.username:
                if user.password == self.password:
                    return True
        return False

    def logout(self):
        print ("User logged out")

    def create_comment(self, text):
        comment = Comment(text, self.username)
        comments.append(comment)

