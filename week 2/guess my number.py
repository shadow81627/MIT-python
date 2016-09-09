# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:22:28 2016

@author: Robinson
"""

print("Please think of a number between 0 and 100!")
#initialise the varible for the input to be stored in
input = " "

#bottom end of the range to guess between
low = 0

#top end of the range to guess between
high = 100

#initialise of the number the program will guess as the middle point of the range
number =  int((high - low)/2)

#
while input != "c":
    print("Is your secret number " + str(number) + "?")
    