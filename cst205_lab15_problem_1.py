#!/usr/bin/python
# CST205 Lab 15 Problem 1
# December 7, 2017
#
# Team 5, Hopper
#  Grace Alvarez
#  Gabriel Loring

import random

NUMBER_OF_DICE = 2                        # Problem supplied constant
NUMBER_OF_SIDE_DICE = 6                   # Problem supplied constant
FIRST_ROLL_WINNING_OUTCOMES = [7, 11]     # Problem supplied rules
FIRST_ROLL_LOOSING_OUTCOMES = [2, 3, 12]  # Problem supplied rules
SUBSEQUENT_ROLL_LOOSING_NUMBER = 7        # Problem supplied rule



def craps():
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
    # We have two sets of rules for 1st roll and subsequent rolls
    # the outer if condition is to differentiat between the types of rolls
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

craps()