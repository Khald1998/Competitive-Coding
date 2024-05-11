#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # The "Day of the Programmer" is the 256th day of the year.
    # For the Julian calendar (years before 1918 in Russia), leap years are divisible by 4.
    # For the Gregorian calendar (years after 1918), leap years are either divisible by 400,
    # or divisible by 4 but not by 100.
    
    # In 1918, Russia transitioned from the Julian to the Gregorian calendar,
    # February had 14 days omitted. Therefore, the 256th day is the 26th of September.
    if year == 1918:
        return "26.09.1918"
    
    # Define a function to check if a given year is a leap year in the Julian calendar
    def isJulianLeapYear(year):
        return year % 4 == 0
    
    # Define a function to check if a given year is a leap year in the Gregorian calendar
    def isGregorianLeapYear(year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    
    # If it's a leap year, the 256th day is the 12th of September.
    # If it's not a leap year, the 256th day is the 13th of September.
    if (year < 1918 and isJulianLeapYear(year)) or (year > 1918 and isGregorianLeapYear(year)):
        return "12.09." + str(year)
    else:
        return "13.09." + str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
