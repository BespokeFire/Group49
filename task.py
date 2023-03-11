import math


def my_func():
    return "Hello World"


def my_datetime(num_sec):
    # set up month, day, year
    month = 1
    day = 1
    year = 1970

    day_secs = 24*60*60
    yr_secs = (365.2425*day_secs)

    # Estimate what year we're in
    add_years = math.floor(num_sec/yr_secs)
    year += add_years

    # stringify month and day - check if 0 needs to be added
    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)

    if day < 10:
        day = "0" + str(day)
    else:
        day = str(day)

    return month + "-" + day + "-" + str(year)


def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0 and year % 400 != 0:
        leap = False
    return leap


def numLeaps(year):
    return
