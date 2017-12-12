#!/usr/bin/python
# CST205 Lab 15 Problem 2
# December 7, 2017
#
# Team 5, Hopper
#  Grace Alvarez
#  Gabriel Loring


import datetime
import calendar

weekdayNames = [ "Monday", "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday", "Sunday"]

# Print out a calendar of the month you were born
def printCalendarByYearMonth(year=1970,month=1):
  '''
  Use python to print out a calander for a 
  given year and month
  '''
  if month not in range(1,13):
    print(month)
    raise
  c = calendar.TextCalendar(calendar.SUNDAY)
  c.prmonth(year, month) 
   
def datesTillDate(month, day):
  '''
  Use python date math to compute difference between
  two month / days.  Make sure not to compute a negatie
  if the current month is greater then the target month
  then we need to set our target year to current year + 1
  '''
  today = datetime.datetime.now()
  current_year = today.year
  current_month = today.month
  current_Day = today.day
  
  # see if there birthday has already passed this year  
  if current_month >= month:
    year = current_year + 1
  else:
    year = current_year
    
  dateCurrent = datetime.datetime(current_year,current_month,current_Day)
  dateFuture = datetime.datetime(year,month,day)
  return (dateFuture - dateCurrent).days
  
def dayOfTheWeekFromDate(month=1, day=1, year=1970):
  '''
  Use a dictionary to convert between pythons methode of returning
  an integer to represent day of the week to the problem requirment
  that we return the english name of the day of the week
  '''
  return weekdayNames[datetime.date(year, month, day).weekday()]


def main():
  '''
  Execute all the problems for the lab
  '''
  
  #Get user information
  birthday= requestString("Enter your birthday  MM/DD/YYYY\n")
  dateElements = birthday.split("/")
  year = int(dateElements[2])
  day = int(dateElements[1])
  month = int(dateElements[0])
 
  #Problem 1
  print("Here is the calendar for the month you were born\n")
  printCalendarByYearMonth(year=year,month=month)

  #Problem 2
  print("\nDays until your next birthday: %i"%datesTillDate(month=month, day=day))
  
  #Problem 3
  independenceDay = "7/4/1776"
  dateElements = independenceDay.split("/")
  year = int(dateElements[2])
  day = int(dateElements[1])
  month = int(dateElements[0])  
  print("The declaration of independence was signed on %i/%i/%i a %s"%(month,day,year,dayOfTheWeekFromDate(month=month, day=day, year=year)))

  
main()
