#!/usr/bin/python
# CST205 Lab 15 Problem 2
# December 7, 2017
#
# Team 5, Hopper
#  Grace Alvarez
#  Gabriel Loring


'''
Problem 2:
Have some fun with different library functions by figuring out how to get Python to:

Print out a calendar of the month you were born
Tell you how many days it is until your next birthday
What day of the week was the Declaration of Independence ratified by the Continental Congress? (write a program that prints out Monday, Tuesday, etc)
'''


import calendar
'''
year = 1973
day = 28
month = 10
x = calendar.setfirstweekday(calendar.SUNDAY)
c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(year, month)
'''
# Print out a calendar of the month you were born
def printCalendarByYearMonth(year=1970,month=1):
  if month not in range(1,13):
    print(month)
    raise
  c = calendar.TextCalendar(calendar.SUNDAY)
  c.prmonth(year, month) 
   
def datesTillDate(month, day):
  current_year = 2017
  current_month = 12
  current_Day = 1
  
  # see if there birthday has already passed this year  
  if current_month > month:
    year = current_year + 1
  else:
    year = current_year
    
  birthday_year
  d1 = datetime.datetime(current_year,current_month,current_Day)
  d2 = datetime.datetime(year,month,day)
  return 1
  
def dayOfTheWeekFromDate(month=1, day=1, year=1970):
  return 1


def main():
  #Get user information
  print("Enter your birthday  MM/DD/YYYY\n")
  birthday = "10/28/1973"
  dateElements = birthday.split("/")
  year = int(dateElements[2])
  day = int(dateElements[1])
  month = int(dateElements[0])
 
  #Problem 1
  print("Here is the calendar for the month you were born")
  printCalendarByYearMonth(year=year,month=month)

  #Problem 2
  print("Days until your next birthday: %i"%datesTillDate(month=month, day=day))
  
  #Problem 3
  independenceDay = "7/4/1776"
  dateElements = independenceDay.split("/")
  year = int(dateElements[2])
  day = int(dateElements[1])
  month = int(dateElements[0])  
  print("The declaration of independence was signed on %i/%i/%i a %s"%(month,day,year,dayOfTheWeekFromDate(month=month, day=day, year=year)))

  
main()
