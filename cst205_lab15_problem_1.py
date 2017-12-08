#!/usr/bin/python
# CST205 Lab 15 Problem 1
# December 7, 2017
#
# Team 5, Hopper
#  Grace Alvarez
#  Gabriel Loring

'''
Problem 1:

Use a function from the random library to simulate rolling dice.  Write a function that rolls a single die and then use that function to build a program that let's the user play craps. The basic rules of craps are:

1. A player rolls two six-sided dice and adds the numbers rolled together.
2. On this first roll, a 7 or an 11 automatically wins, and a 2, 3, or 12 automatically loses, and play is over. If a 4, 5, 6, 8, 9, or 10 are rolled on this first roll, that number becomes the "point.???
3. The player continues to roll the two dice again until one of two things happens: either they roll the "point" again, in which case they win; or they roll a 7, in which case they lose.
'''

import random

NUMBER_OF_DICE = 2
NUMBER_OF_SIDE_DICE = 6
FIRST_ROLL_WINNING_OUTCOMES = [7, 11]
FIRST_ROLL_LOOSING_OUTCOMES = [2, 3, 12]
SUBSEQUENT_ROLL_LOOSING_NUMBER = 7

rollCount = 1
gameContinue = True
gameWin = False
thePointNumber = 0
diceOutcome=[0,0]

while gameContinue:
  # Problem Bullet 1
  for x in range(NUMBER_OF_DICE):
    diceOutcome[x] = random.randint(1,NUMBER_OF_SIDE_DICE)
    
  sumOfDice = diceOutcome[0] + diceOutcome[1]
  
  # Check for outcomes based on roll number and dice sum
  if rollCount == 1:
    if sumOfDice in FIRST_ROLL_WINNING_OUTCOMES:
      print "Lucky! You won with a %i and %i = %i"%(diceOutcome[0], diceOutcome[1], sumOfDice )
      gameContinue = False
    elif sumOfDice in FIRST_ROLL_LOOSING_OUTCOMES:
      gameContinue = False
      print "Sorry you lost on the first roll with a %i and %i = %i"%(diceOutcome[0], diceOutcome[1], sumOfDice )
    else:
      thePointNumber = sumOfDice
      print "No matches on the first roll, %i and %i = %i the point number is %i, Roll again!"%(diceOutcome[0], diceOutcome[1], sumOfDice,thePointNumber)
  else:
    if sumOfDice == SUBSEQUENT_ROLL_LOOSING_NUMBER:
      gameContinue = False
      print "Sorry you lost with a %i and %i = %i"%(diceOutcome[0], diceOutcome[1], sumOfDice )
    elif sumOfDice == thePointNumber:
      print "You won! A %i and %i = %i the point number was %i"%(diceOutcome[0], diceOutcome[1], sumOfDice,thePointNumber)
      gameContinue = False
    else:
      print "No matches, %i and %i = %i the point number is %i, Roll again!"%(diceOutcome[0], diceOutcome[1], sumOfDice,thePointNumber)
  
  rollCount = rollCount + 1  

  