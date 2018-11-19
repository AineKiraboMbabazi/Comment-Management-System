from User import User




class Moderator(User):
    def __init__(self):
        super.__init__(self.username, self.password)
        self.is_moderator = True
