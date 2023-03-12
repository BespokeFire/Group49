import math

def conv_num(num_str):
    """
    Converts a string representation of an int/float/hex to an int or float. 
    """
    
    # Make sure that the input is a non-empty string. 
    
    try:
        _ = str(num_str)    
    except:
        return None
    
    if len(num_str) == 0:
        return None
    
    # Convert the string into lowercase.
    
    num_str = to_lower(num_str)
    
    
    # Check the sign of the number in the string, Remove the sign from the string and Store it in a variable
    
    if starts_with_sign(num_str):
        sign = -1 if num_str[0] == "-" else 1
        num_str = num_str[1:]
    else:
        sign = 1
    
    # Check if the string is a hexadecimal
    
    if num_str.startswith("0x"):
        for char in num_str[2:]:
            if not is_hex_digit(char):
                return None
        return sign * int(num_str[2:], 16)
    
    # Track the number of decimal points in the string 
    
    decimal_point_count = 0
    
    for i, char in enumerate(num_str):
        if char == ".":
            decimal_point_count += 1
            if decimal_point_count > 1:
                return None
        elif not is_digit(char):
            return None
    
    # Return the converted string
    
    return sign * float(num_str) if decimal_point_count == 1 else sign * int(num_str)

#HELPER FUNCTIONS FOR conv_num
    
def to_lower(string):
    """
    Converts string to all lowercase
    """
    
    lower_string = ""
    
    for char in string:
        if ord(char) >= 65 and ord(char) <= 90:
            lower_string += chr(ord(char) + 32)
        else:
            lower_string += char
    
    return lower_string

    
def starts_with_sign(string):
    """
    Checks the sign in string
    """

    return string[0] == "+" or string[0] == "-"


def is_hex_digit(char):
    """
    Checks if a character is a valid hexadecimal digit
    """
    
    return char in "0123456789abcdef"

def is_digit(char):
    """
    Checks if character is a digit based on ASCII code
    """
    
    return ord(char) >= 48 and ord(char) <= 57

# ----- end of conv_num() implementation -----


def my_func():
    return "Hello World"


def my_datetime(num_sec):
    """ This function takes in an integer representing a number of seconds
    since the epoch 01-01-1970 and returns the corresponding datetime
    taking leap years into account"""

    # set up month, day, year
    month = 1
    day = 1
    year = 1970
    day_secs = 24*60*60
    yr_secs = (365.242189*day_secs)

    # Estimate what year we're in
    add_years = math.floor(num_sec/yr_secs)
    year += add_years

    # Find how many leap years there have been since 1970
    pst_lps = numLeaps(year)

    # check if the current year is a leap year and if so account for it
    is_lp = is_leap(year)
    if is_lp:
        pst_lps -= 1
    was_lp = is_lp

    # subtract leap days from total seconds
    lp_secs = pst_lps * day_secs
    num_sec -= lp_secs

    # recalculate the year
    add_years = math.floor(num_sec/(365*day_secs))
    year = 1970 + add_years
    is_lp = is_leap(year)
    up_pst_lp = numLeaps(year)

    # resolve NYE on leap year edge case
    if is_lp:
        up_pst_lp -= 1

    if was_lp is True and is_lp is False:
        rm_days = math.floor((num_sec % (365*day_secs)) / day_secs) + 1
        if rm_days == 1:
            year -= 1
            return "12-31-" + str(year)

    if was_lp is False and is_lp is True and up_pst_lp < pst_lps:
        was_lp = is_lp
        num_sec += day_secs
        add_years = math.floor(num_sec/(365*day_secs))
        year = 1970 + add_years
        is_lp = is_leap(year)
        if was_lp is True and is_lp is False:
            rm_days = math.floor((num_sec % (365*day_secs)) / day_secs) + 1
            if rm_days == 1:
                year -= 1
                return "12-31-" + str(year)

    # get how many days have passed in the year
    rm_days = math.floor((num_sec % (365*day_secs)) / day_secs)
    rm_days += day
    day, mnth = findMo(is_lp, rm_days)
    month += mnth

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
    """ Helper function to my_datetime() that takes in an integer representing
    a given year and returns True if it is a leap year and False otherwise"""
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0 and year % 400 != 0:
        leap = False
    return leap


def numLeaps(year):
    """ Helper function to my_datetime() that takes in an integer representing
    a given year and returns the number of leap years that have happened
    including the given year if it is a leap year"""
    cur = (year // 4) - (year // 100) + (year // 400)
    pst = 477  # 477 represents the number of leap years prior to 1970
    return cur - pst


def findMo(is_leap, days):
    """ Helper function to my_datetime() that takes in a bool representing
    whether or not it's a leap year and an integer representing
    the days of the year that have passed and returns the month and day of
    the year"""
    mo = 0
    if is_leap is False:
        mos = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        mos = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while days > mos[mo]:
        days -= mos[mo]
        mo += 1

    return (days, mo)

# ----- end of my_datetime() implementation -----
