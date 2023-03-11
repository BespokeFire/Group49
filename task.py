def my_func():
    return "Hello World"


def my_datetime(num_sec):
    # set up month, day, year
    month = 1
    day = 1
    year = 1970

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
