def is_leap(chose_year):
    """Take the year value, and it returns True if the year is a leap year or False if the year is Not leap year"""
    if chose_year % 4 == 0:
        if chose_year % 100 == 0:
            if chose_year % 400 == 0:
                return True  # Leap year
            return False  # Not Leap year
        return True  # Leap year
    return False  # Not Leap year


def days_in_month(interested_year, interested_month):
    if interested_month < 0 or interested_month > 12:
        return "Not validate month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    if is_leap(interested_year) and interested_month == 2:
        print("leap year!")
        return 29
    else:
        print("Not leap year!")
        return month_days[interested_month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
