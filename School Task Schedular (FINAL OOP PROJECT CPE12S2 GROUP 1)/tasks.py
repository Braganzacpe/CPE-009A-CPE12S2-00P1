from models   import Task
from school_calendar import calendar, find_day, ask_date
from utils    import MONTHS, GREEN, RED, RESET, show_header, notify, pause
from auth     import student_creds

def add_task(user):
    month, day_num = ask_date(user, "Teacher")
    day            = find_day(month, day_num)
    date_label     = f"{MONTHS[month - 1]} {day_num}"
    slots_left     = 10 - len(day.tasks)

    show_header(f"Add Tasks - {date_label}", user, "Teacher")

    if slots_left <= 0:
        notify("Day is full! (Max 10)", False)
        return

    print(f"Slots: {len(day.tasks)}/10\n")

    try:
        count = int(input(f"Task Quantity (max {slots_left}): "))
        if count <= 0 or count > slots_left:
            raise ValueError
    except:
        notify("Invalid.", False)
        return

    for i in range(count):
        show_header(f"Task {len(day.tasks) + 1}/10 - {date_label}", user, "Teacher")
        name     = input("Task Description: ")
        deadline = input("Deadline: ")
        day.tasks.append(Task(name, deadline, owner=user))

    notify(f"Added {count} task(s) for {date_label}.")

def view_tasks_teacher(user):
    from utils import BLUE
    show_header("My Tasks", user, "Teacher")

    # ── My tasks ────────────────────────────────────────────
    my_found = False

    for month in range(12):
        for week in calendar[month]:
            for day in week:
                if day.day == 0:
                    continue
                my_tasks = [t for t in day.tasks if t.owner == user]
                if not my_tasks:
                    continue
                my_found = True
                print(f"\n{MONTHS[month]} {day.day}")
                for task in my_tasks:
                    total_students = len(student_creds)
                    students_done  = len(task.done_by)
                    if total_students == 0 or students_done < total_students:
                        status = f"{RED}Pending{RESET}"
                    else:
                        status = f"{GREEN}All Done{RESET}"
                    print(f"  - {task.name}")
                    print(f"    Deadline : {task.deadline}")
                    print(f"    Status   : {status}")

    if not my_found:
        print("\n  No tasks yet.")

    # ── Other teachers' tasks ────────────────────────────────
    print(f"\n{'─'*40}")
    print(" Other Teacher's Tasks".center(40))
    print(f"{'─'*40}")
    other_found = False

    for month in range(12):
        for week in calendar[month]:
            for day in week:
                if day.day == 0:
                    continue
                other_tasks = [t for t in day.tasks if t.owner != user]
                if not other_tasks:
                    continue
                other_found = True
                print(f"\n{MONTHS[month]} {day.day}")
                for task in other_tasks:
                    total_students = len(student_creds)
                    students_done  = len(task.done_by)
                    if total_students == 0 or students_done < total_students:
                        status = f"{RED}Pending{RESET}"
                    else:
                        status = f"{GREEN}All Done{RESET}"
                    print(f"  - {task.name}")
                    print(f"    Deadline : {task.deadline}")
                    print(f"    Owner    : {BLUE}{task.owner}{RESET}")
                    print(f"    Status   : {status}")

    if not other_found:
        print("\n  No tasks from other teachers yet.")

    pause()

def view_tasks_student(user):
    show_header("My Tasks", user, "Student")
    found = False

    for month in range(12):
        for week in calendar[month]:
            for day in week:
                if day.day == 0 or not day.tasks:
                    continue
                found = True
                print(f"\n{MONTHS[month]} {day.day}")
                for task in day.tasks:
                    if user in task.done_by:
                        status = f"{GREEN}Done{RESET}"
                    else:
                        status = f"{RED}Pending{RESET}"
                    print(f"  - {task.name}")
                    print(f"    Deadline : {task.deadline}")
                    print(f"    Status   : {status}")

    if not found:
        print("\nNo tasks yet.")

    pause()

def mark_done(user):
    show_header("Mark Done", user, "Student")
    pending = []

    for month in range(12):
        for week in calendar[month]:
            for day in week:
                if day.day == 0:
                    continue
                for task in day.tasks:
                    if user not in task.done_by:
                        pending.append((task, MONTHS[month], day.day))

    if not pending:
        print("\nAll done!")
        pause()
        return

    for i, (task, month_name, day_num) in enumerate(pending):
        print(f"{i + 1}. {task.name}  ({month_name} {day_num})")

    try:
        choice = int(input("\nWhich task? ")) - 1
        if not (0 <= choice < len(pending)):
            raise ValueError
        pending[choice][0].done_by.add(user)
        notify("Marked as done!")
    except:
        notify("Invalid.", False)

def delete_task(user):
    show_header("Delete Task", user, "Teacher")
    my_tasks = []

    for month in range(12):
        for week in calendar[month]:
            for day in week:
                if day.day == 0:
                    continue
                for task in day.tasks:
                    if task.owner == user:
                        my_tasks.append((task, day, MONTHS[month], day.day))

    if not my_tasks:
        notify("No tasks found.", False)
        return

    for i, (task, day, month_name, day_num) in enumerate(my_tasks):
        print(f"{i + 1}. {task.name}  ({month_name} {day_num})")

    try:
        raw = input("\nSelect to delete (Enter to go back):\n").strip()
        if raw == "":
            return
        
        choice = int(raw) - 1
        
        if not (0 <= choice < len(my_tasks)):
            raise IndexError
            
        task, day, month_name, day_num = my_tasks[choice]
        day.tasks.remove(task)
        notify("Deleted!")
        
    except (ValueError,IndexError):
        notify("Invalid input.", False)
        