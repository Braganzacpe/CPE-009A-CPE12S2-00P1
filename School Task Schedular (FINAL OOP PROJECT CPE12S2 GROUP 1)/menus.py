from utils     import show_header, notify
from school_calendar  import show_calendar
from tasks     import add_task, view_tasks_teacher, view_tasks_student, mark_done, delete_task

def teacher_menu(user):
    while True:
        show_header("Teacher Menu", user, "Teacher")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Calendar")
        print("5. Logout")

        choice = input("\nChoice: ")

        if choice == "1":
            add_task(user)
        elif choice == "2":
            view_tasks_teacher(user)
        elif choice == "3":
            delete_task(user)
        elif choice == "4":
            show_calendar(user, "Teacher")
        elif choice == "5":
            break
        else:
            notify("Invalid.", False)

def student_menu(user):
    while True:
        show_header("Student Menu", user, "Student")
        print("1. View Tasks")
        print("2. Mark Done")
        print("3. Calendar")
        print("4. Logout")

        choice = input("\nChoice: ")

        if choice == "1":
            view_tasks_student(user)
        elif choice == "2":
            mark_done(user)
        elif choice == "3":
            show_calendar(user, "Student")
        elif choice == "4":
            break
        else:
            notify("Invalid.", False)
