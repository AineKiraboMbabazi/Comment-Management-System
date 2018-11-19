
from User import User
from Comment import Comment
from database import users, comments


def main():
    username = str(raw_input("Enter your Username"))
    password = str(raw_input("Enter password"))

    user = User(username, password)
    user.signup(user)


    login_prompt = input("Would You like to Login?  Enter: 1 for YES, 0 for NO ")
    if login_prompt == 1:
        username = input("Enter Username: ")
        password = input("Enter your password: ")

        is_logged_in = User.login(username, password)
        if is_logged_in:
            text = input("Enter your comment: ")
        else:
            print("You are not logged in: ")
            return
    else:
        print ("Please login to comment: ")
        return 0

    user.create_comment(text)

    for comment in comments:
        commentsList = {'username':comments.username, 'text':comment.text, 'timestamp':comment.timestamp}
        print(commentsList)

main()