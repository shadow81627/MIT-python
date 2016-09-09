# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 16:22:28 2016

@author: Damien Robinson
"""

print("Please think of a number between 0 and 100!")

#bottom end of the range to guess between
low = 0
#top end of the range to guess between
high = 100

#the varible used to tell if we should keep guessing
guessed =  False

#if the guess is not correct then keep guessing
while not guessed:
    #Bisectional search
    guess = (high + low)//2
    print("Is your secret number " + str(guess)+ "?")
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_input == "c" or high - low == 1:
        #guess is correct
        guessed = True
    elif user_input == "h":
        #guess is too high set the top of the search range to be guess
        high = guess
    elif user_input == "l":
        #guess is too low set the bottow of the search range to be guess
        low = guess
    else:
        print("Sorry, I did not understand your input.")
    
print("Game over. Your secret number was: " + str(guess))
