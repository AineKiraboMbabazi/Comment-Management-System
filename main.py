
from User import User
from Comment import Comment
from database import users, comments


def main():
    username = str(raw_input("Enter your Username"))
    password = str(raw_input("Enter password"))

    user = User(username, password)
    user.signup(user)


    login_prompt = raw_input("Would You like to Login?  Enter: 1 for YES, 0 for NO ")
    # text = "jb"
    if login_prompt == 1:
        username = raw_input("Enter Username: ")
        password = raw_input("Enter your password: ")

        is_logged_in = user.login()
        if is_logged_in:
            text = str(raw_input("Enter your comment: "))
        else:
            print("You are not logged in: ")
            return
    else:
        print ("Please login to comment: ")
        return 0

    user.create_comment(text)

    for comment in comments:
        print({'id': comment.id,'username': comment.username, 'text':comment.text, 'timestamp':comment.timestamp})


    edit_ = input("Do you want to add another comment, edit or delete: 1 , 2 or 3")
    if edit_ == 2:
        get_id = input("Enter comment Id")
        new_comment = str(input("Enter new comment"))
        for item in comments:
            if item.id == get_id:
                item.text = new_comment
        print("Your comment was updated.")
    if edit_ == 3:
        get_id = input("Enter comment Id")
        for item in comments:
            if item.id == get_id:
                item.remove(get_id)
        print ("Your comment was deleted")


main()