#!/usr/bin/python
# CST205 Lab 16
# December 7, 2017
#
# Team 5, Hopper
#  Grace Alvarez
#  Gabriel Loring



'''
Ok, now that we can read from a URL, get data out of the html (Just like in the headline lab), and write a page, we can finally get started on the lab itself.  For today's lab
	Choose a website that you frequent that has data (text) that could be scraped from it's HTML (this could be Facebook, CNN, Kitty Pictures, whatever)
	Write some code that collects at least 10 pieces of information from the webiste (e.g. friends from Facebook, or headlines from CNN, comments on kitty pictures, etc)
	Create a new web page that displays ONLY the information you collected in step 2
The page you create can be very simple. You only need to display the information in a readable format.  No fancy formatting required ... we'll save that for next time :)
To get checked off, be prepared to show:
	The original website you got your data from
	Your code in lab16_LastName.py format (Please add your name and your partner's name as a comment in the beginning of your program. )
	Your resulting html page that you created
'''
import urllib
#import re
import os

#PROBLEM 1

def makePage():
  #replace the directory in the line below with the path to your file
  #file = open("C:\Users\Grace\Desktop\CSUMB\CST205\Module 8\Lab 16\super.html", "wt")
  completeFilePath = os.path.join( os.path.dirname(os.path.realpath(__file__)), "super.html")
  file = open(completeFilePath, "wt")
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>
  <h1>MY PYTHON PAGE!!!</h1>
  </body>
  </html>""")
  
  file.close()
  

#PROBLEM 2

def web():
    news = urllib.urlopen('http://www.cnn.com').read()
    #file = open("C:\Users\Grace\Desktop\CSUMB\CST205\Module 8\Lab 16\super.html", "wt")
    completeFilePath = os.path.join( os.path.dirname(os.path.realpath(__file__)), "super.html")
    file = open(completeFilePath, "wt")    
    file.write("""<!DOCTYPE html>
    
    <html>
    <head><title>CNN Headlines</title></head>
    
            
    <body>
    <h2 style='text-align:center;'>CNN Headlines</h2>
    
    <td>
    <ul class='strong'>""")
        
    
    #Searching for headlines starting with <strong> tag and ending with </strong> tag
    i = 0
    news = news.replace("\\u003c", "<") # Headline tags can appear <strong> or \\u003cstrong>, this makes them uniform,same with closeing tag
    start = "<strong>"
    end = "</strong>"

    #create empty list called headers
    #while the index is less than or equal to the length of the news file
    #search for headers with starting tag "<strong>"  
    headers = []
    while i <= len(news):
      tag = news.find(start, i, len(news))
      if tag == -1:
        break
    
      #new string starts at tag <strong>
      #then search for the end tag </strong>
      news = news[tag:len(news)+1]
      tag = news.find(end, len(end), len(news))
      
      #adds a new header string to the headers list each time <strong> text </strong) is found
      #increment index i so we can continue to the next set of <strong> tags
      string = news[len(end)-1:tag]
      i += tag
      headers.append(string)
  
    for text in headers:
      file.write("<li><h3>" + text + "</h3></li><br />")          
      

    file.write("""  

    </ul>
    </td>
    </body>
    </html>""")
    file.close()
    
web()
