#!/usr/bin/python
'''
All the years that are perfectly divisible by 4 are called as Leap years except the century years.
Century year's means they end with 00 such as 1200, 1300, 2400, 2500 etc (Obviously they are divisible by 100).
For these century years we have to calculate further to check the Leap year:
If the century year is divisible by 400 then that year is a Leap year
If the century year is not divisible by 400 then that year is a Not Leap year
'''
#V1: This code reads input from user and test for leap year
num=int(input("Enter Year:"))

def leap_year(year):
    return ( year % 4 == 0 and year % 100 != 0) or year % 400 == 0

print num,"is leap year" if leap_year(num) else "not a leap year"

#V2 use calender module
#import calendar
#print calendar.isleap(num)
