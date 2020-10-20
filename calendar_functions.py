# Isabella Gomez A15305555
# ECE143 HW3

# Instructions:
# Write a function that returns the number of calendar days in a given year and month.

import calendar
def number_of_days(year,month):
    '''
    Function will take the year and month and return the total number of days in
    that month.

    :param year: year wanted to be counted
    :param month: month which days are counted from
    :return: number of days in a given month
    '''

    # check year and month are type int
    assert type(year) == int
    assert type(month) == int

    # check month and year is within constraints
    assert month >= 1 and month <=12
    assert year >= 0

    number_of_days = calendar.monthlen(year, month)

    return number_of_days

# Instructions:
# Write a function to find the number of leap-years between (including both
# endpoints) two given years.

def number_of_leap_years(year1,year2):
    '''
    Function returns the number of leap-years between two given years.

    :param year1: start of range of years
    :param year2: end of range of years
    :return: number of leap years
    '''

    # check that year1 and year2 are ints
    assert type(year1) == int
    assert type(year2) == int

    # check that the years are not negative
    assert year1 >= 0
    assert year2 >= 0

    num_leap_years = calendar.leapdays(year1,year2)

    return num_leap_years

# Instructions:
# Write a function to find the string name (e.g., Monday, Tuesday) of the day of the
# week on a given month, day, and year.

def get_day_of_week(year,month,day):
    '''
    Function uses the year, month, and day to find and return the name of the weekday
    in a string.

    :param year:
    :param month:
    :param day:
    :return: string of weekday name
    '''

    # check year, month, day are type int
    assert type(year) == int
    assert type(month) == int
    assert type(day) == int

    # check they are within constraints
    assert day >= 1 and day <=31
    assert month >= 1 and month <= 12
    assert year >= 0

    weekday_num = calendar.weekday(year, month, day)

    # change weekday_num to string
    if weekday_num == 0:
        weekday = "Monday"
    elif weekday_num == 1:
        weekday = "Tuesday"
    elif weekday_num == 2:
        weekday = "Wednesday"
    elif weekday_num == 3:
        weekday = "Thursday"
    elif weekday_num == 4:
        weekday = "Friday"
    elif weekday_num == 5:
        weekday = "Saturday"
    elif weekday_num == 6:
        weekday = "Sunday"

    return weekday

