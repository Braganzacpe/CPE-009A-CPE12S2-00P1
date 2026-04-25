from models import Day
from utils  import MONTHS, BLUE, RESET, show_header, pause

year     = 2026
calendar = [[[Day() for _ in range(7)] for _ in range(6)] for _ in range(12)]

def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

def days_in_month(month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 1 and is_leap_year(year):
        return 29
    return days[month]

def get_start_day(month):
    m, y = month + 1, year
    if m < 3:
        m += 12
        y -= 1
    k = y % 100
    j = y // 100
    return ((1 + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7 + 6) % 7

def build_calendar():
    for month in range(12):
        day_of_week = get_start_day(month)
        week        = 0
        for day_num in range(1, days_in_month(month) + 1):
            calendar[month][week][day_of_week].day = day_num
            day_of_week += 1
            if day_of_week > 6:
                day_of_week = 0
                week += 1

def find_day(month, day_num):
    for week in calendar[month - 1]:
        for day in week:
            if day.day == day_num:
                return day

def ask_date(user=None, role=None):
    from utils import notify
    while True:
        try:
            show_header("Enter Date", user, role)
            month   = int(input("Month (1-12): "))
            day_num = int(input("Day: "))
            if 1 <= month <= 12 and 1 <= day_num <= days_in_month(month - 1):
                return month, day_num
            notify("Invalid date.", False)
        except:
            notify("Numbers only.", False)

def show_calendar(user=None, role=None):
    show_header("Calendar", user, role)
    for month in range(12):
        print(f"\n{MONTHS[month]} {year}")
        print("Su Mo Tu We Th Fr Sa")
        for week in calendar[month]:
            if all(day.day == 0 for day in week):
                break
            row = ""
            for day in week:
                if day.day == 0:
                    row += "   "
                elif day.tasks:
                    row += f"{BLUE}[{day.day:2}]{RESET}"
                else:
                    row += f"{day.day:2} "
            print(row)
    pause()
