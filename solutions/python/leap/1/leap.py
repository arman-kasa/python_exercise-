def leap_year(year):
    """Determine whether a year is a leap year in the Gregorian calendar."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
