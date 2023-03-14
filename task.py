import math


def conv_num(num_str):
    """
    Converts a string representation of a number to an integer or a float.
    """

    if num_str is None or len(num_str) == 0:
        return None

    # We first convert the string to all lower case
    num_str = to_lower(num_str)

    # We then check the sign of the number in the string, and then remove the
    # sign from it after storing it in a variable
    if starts_with_sign(num_str):
        sign = -1 if num_str[0] == "-" else 1
        num_str = num_str[1:]
    else:
        sign = 1

    # check if the string starts with "0x"
    if num_str.startswith("0x"):
        for char in num_str[2:]:
            if not is_hex_digit(char):
                return None
        return sign * hex_to_int(num_str[2:])

    # track of the number of decimal points in the string
    decimal_point_count = 0
    for i, char in enumerate(num_str):
        if char == ".":
            decimal_point_count += 1
            if decimal_point_count > 1:
                return None
        elif not is_digit(char):
            return None

    # return the string as float
    if decimal_point_count == 0:
        return sign * str_to_int(num_str)
    else:
        int_part, frac_part = num_str.split(".")
        int_val = sign * str_to_int(int_part)
        if len(frac_part) == 0:
            frac_val = 0.0
        else:
            frac_val = sign * str_to_frac(frac_part)
            frac_val = round(frac_val, len(frac_part))
        return int_val + frac_val


# helper functions

def to_lower(string):
    """
    converts a string to lowercase
    """
    return "".join([chr(ord(char) + 32) if 65 <= ord(char) <= 90 else char
                    for char in string])


def starts_with_sign(string):
    """
    checks the sign in string
    """
    return string.startswith("+") or string.startswith("-")


def is_hex_digit(char):
    """
    checks if a character is a valid hexadecimal digit
    """
    return char in "0123456789abcdefABCDEF"


def is_digit(char):
    """
    check if a character is a digit
    """
    return 48 <= ord(char) <= 57


def str_to_int(num_str):
    """
    converts a string of digits to an integer
    """
    num = 0
    for char in num_str:
        num = num * 10 + ord(char) - 48
    return num


def str_to_frac(num_str):
    """
    converts a string of digits representing a fraction to a float
    """
    frac = 0
    divisor = 10
    for char in num_str:
        frac = frac + (ord(char) - 48) / divisor
        divisor = divisor * 10
    return frac


def hex_to_int(hex_str):
    """
    converts a hexadecimal string to an integer
    """
    hex_str = to_lower(hex_str)
    num = 0
    for char in hex_str:
        if is_digit(char):
            num = num * 16 + ord(char) - 48
        else:
            num = num * 16 + ord(char) - 87
    return num
# ----- end of conv_num() implementation -----


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


def conv_endian(num, endian='big'):
    """Converts decimal to hexadecimal in endian form"""
    # Checks if value is negative
    is_neg = 0
    if (num < 0):
        is_neg = 1
        num *= -1

    # Converts decimal to hex and puts it in a list
    hex_list = dec_to_hex(num)

    if (len(hex_list) == 1):
        return "0" + str(hex_list[0])

    # Converts hex_list to a string of the specified endian form
    if (endian == "big"):
        hex_string = big_endian(hex_list)
    elif (endian == "little"):
        hex_string = little_endian(hex_list)
    else:
        return None

    # Add "-" if num is negative
    if (is_neg == 1):
        hex_string = "-" + hex_string

    return hex_string


def big_endian(hex_list):
    """Converts a hexadecimal list into a string of big-endian form"""
    hex_string = ""
    count = 0
    for i in range(len(hex_list)):
        if (len(hex_list) % 2 == 1 and count == 0):
            hex_string += "0"
            hex_string += str(hex_list[count])
            hex_string += " "
            count += -1
        else:
            hex_string += str(hex_list[count])
            hex_string += str(hex_list[count + 1])
            if (count < len(hex_list) - 2):
                hex_string += " "
        count += 2
        if (count >= len(hex_list)):
            break
    return hex_string


def little_endian(hex_list):
    """Converts a hexadecimal list into a string of little-endian form"""
    hex_string = ""
    temp_string = ""
    count = 0
    for i in range(len(hex_list)):
        if (len(hex_list) % 2 == 1 and count == 0):
            temp_string += "0"
            temp_string += str(hex_list[count])
            hex_string = " " + temp_string
            count += -1
        else:
            temp_string += str(hex_list[count])
            temp_string += str(hex_list[count + 1])
            hex_string = temp_string + hex_string
            if (count < len(hex_list) - 2):
                hex_string = " " + hex_string
        count += 2
        if (count >= len(hex_list)):
            break
        temp_string = ""
    return hex_string


def dec_to_hex(dec):
    """Converts decimal to hexadecimal and returns a list"""
    if (dec == 0):
        return [0]

    hex_list = []
    value = dec
    # Creates list of hexadecimal values from dec
    while (value != 0):
        remainder = (value / 16) - (value // 16)
        value = value // 16
        hex_list.insert(0, int(remainder * 16))

    # Converts values greater than 9 into letters
    for i in range(len(hex_list)):
        if (hex_list[i] - 9 > 0):
            hex_list[i] = chr(hex_list[i] + 55)
    return hex_list
# ----- end of conv_endian() implementation -----
