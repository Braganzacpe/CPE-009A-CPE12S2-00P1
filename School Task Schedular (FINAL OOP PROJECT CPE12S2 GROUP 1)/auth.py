from utils import show_header, notify

student_creds = {}
teacher_creds = {}

def register():
    show_header("Register")
    user = input("Username: ")

    if user in teacher_creds or user in student_creds:
        notify("Username taken.", False)
        return

    pwd  = input("Password: ")
    role = input("[1]Teacher | [2]Student: ")

    if role == "1":
        teacher_creds[user] = pwd
    elif role == "2":
        student_creds[user] = pwd
    else:
        notify("Invalid.", False)
        return

    notify("Registered!")

def login():
    from menus import teacher_menu, student_menu
    show_header("Login")
    user = input("Username: ")
    pwd  = input("Password: ")
    role = input("[1]Teacher | [2]Student: ")

    if role == "1" and teacher_creds.get(user) == pwd:
        teacher_menu(user)
    elif role == "2" and student_creds.get(user) == pwd:
        student_menu(user)
    else:
        notify("Wrong username or password.", False)
