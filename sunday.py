import time
from math import floor

"""
Gaussian algorithm to determine day of week
"""
def day_of_week(year, month, day):
    d = day
    m = (month - 3) % 12 + 1
    y = year % 100
    c = (year - (year % 100)) / 100

    w = (d + floor(2.6 * m - 0.2) + y + floor(y/4) + floor(c/4) - 2*c) % 7

    return int(w)

"""
Compute the number of months starting on a given day of the week in a century
"""
def months_start_range(day,year_start,year_end):
    total = 0
    for year in range(year_start, year_end + 1):
        for month in range(1,13):
            if day_of_week(year, month, 1) == day: total += 1
    #return total
    print(total)
