import os, time

GREEN = "\033[92m"
RED   = "\033[91m"
BLUE  = "\033[94m"
RESET = "\033[0m"
LINE  = "─" * 40

MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue...")

def notify(msg, ok=True):
    color = GREEN if ok else RED
    print(f"\n{color}{msg}{RESET}")
    time.sleep(1)

def show_header(title, user=None, role=None):
    clear()
    print(LINE)
    print(title.center(40))
    print(LINE)
    if user and role:
        color = BLUE if role == "Teacher" else GREEN
        print(f"{color}{user}{RESET} [{role}]")
        print(LINE)
