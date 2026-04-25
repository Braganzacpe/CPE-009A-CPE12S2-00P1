from school_calendar import build_calendar
from auth     import register, login
from utils    import show_header, notify

def main():
    build_calendar()

    while True:
        show_header("School Task Scheduler")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nChoice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            notify("Invalid Input.", False)

if __name__ == "__main__":
    main()
