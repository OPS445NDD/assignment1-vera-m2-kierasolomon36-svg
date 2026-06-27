#!/usr/bin/env python3
"""
OPS445 Assignment 1 - Final Submission
Author: Kiera Solomon
"""
import sys

def day_of_week(year: int, month: int, date: int) -> str:
    """Based on the algorithm by Tomohiko Sakamoto"""
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

def leap_year(year: int) -> bool:
    """Return True if the year is a leap year, False otherwise."""
    # Standard calendar rules for century and leap-year boundaries
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def mon_max(month: int, year: int) -> int:
    """Return the maximum number of days in a given month and year."""
    # Check February dynamically based on leap year status
    if leap_year(year):
        feb_max = 29
    else:
        feb_max = 28

    mon_dict = {1: 31, 2: feb_max, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return mon_dict[month]

def after(date: str) -> str:
    """Return the date for the next day of the given date."""
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    max_days = mon_max(month, year)
    tmp_day = day + 1  

    # Check for month or year rollover boundaries
    if tmp_day > max_days:
        to_day = 1
        to_month = month + 1     
        if to_month > 12:
            to_month = 1
            year += 1
    else:
        to_day = tmp_day
        to_month = month

    next_date = f"{year}-{to_month:02d}-{to_day:02d}"
    return next_date

def valid_date(date: str) -> bool:
    """Check validity of date string and return True if valid, False otherwise."""
    # Ensure correct structural layout length
    if len(date) != 10:
        return False
    if date[4] != '-' or date[7] != '-':
        return False

    # Prevent crash if non-integers are submitted
    try:
        str_year, str_month, str_day = date.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
    except ValueError:
        return False

    # Check boundary limits for months and days
    if month < 1 or month > 12:
        return False

    if day < 1 or day > mon_max(month, year):
        return False

    return True

def usage():
    """Print a helpful message to the user when they make a mistake, and exit."""
    print("Usage: " + sys.argv[0] + " YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

def day_count(start_date: str, stop_date: str) -> int:
    """Loops through range of dates inclusive, and returns number of weekend days."""
    # Verification to ensure lower date is always start_date to prevent an infinite loop
    if start_date > stop_date:
        start_date, stop_date = stop_date, start_date

    weekend_days = 0
    current_date = start_date

    while True:
        str_year, str_month, str_day = current_date.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        # Check day name string and count if it lands on a weekend
        day_str = day_of_week(year, month, day)
        if day_str in ['sat', 'sun']:
            weekend_days += 1

        if current_date == stop_date:
            break

        current_date = after(current_date)

    return weekend_days

if __name__ == "__main__":
    # 1. Check exact number of arguments (Requires script name + 2 dates)
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    stop_date = sys.argv[2]

    # 2. Confirm both provided strings are structurally valid dates
    if not valid_date(start_date) or not valid_date(stop_date):
        usage()

    # 3. For printing purposes, match the chronological display requirements
    if start_date > stop_date:
        print_start, print_stop = stop_date, start_date
    else:
        print_start, print_stop = start_date, stop_date

    # 4. Calculate and display final required string output
    total_weekends = day_count(start_date, stop_date)
    print(f"The period between {print_start} and {print_stop} includes {total_weekends} weekend days.")
