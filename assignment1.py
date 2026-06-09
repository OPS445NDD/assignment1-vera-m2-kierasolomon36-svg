#!/usr/bin/env python3
"""
OPS445 Assignment 1 - Milestone 1
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
    lyear = year % 4
    if lyear == 0:
        feb_max = 29
    else:
        feb_max = 28

    lyear = year % 100
    if lyear == 0:
        feb_max = 28

    lyear = year % 400
    if lyear == 0:
        feb_max = 29
        
    return feb_max == 29

def mon_max(month: int, year: int) -> int:
    """Return the maximum number of days in a given month and year."""
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

    if tmp_day > max_days:
        to_day = tmp_day % max_days  
        tmp_month = month + 1        
    else:
        to_day = tmp_day             
        tmp_month = month + 0        

    if tmp_month > 12:
        to_month = 1                 
        year = year + 1              
    else:
        to_month = tmp_month + 0     

    next_date = f"{year}-{to_month:02}-{to_day:02}"
    return next_date

def usage():
    """Print a usage message to the user."""
    pass

def valid_date(date: str) -> bool:
    """Check validity of date and return True if valid."""
    pass

def day_count(start_date: str, stop_date: str) -> int:
    """Loops through range of dates, and returns number of weekend days."""
    pass

if __name__ == "__main__":
    pass
