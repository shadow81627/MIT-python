# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 15:11:27 2016

@author: Robinson
"""

s = 'zyxwvutsrqponmlkjihgfedcba'
letters = ""
print(letters)
lastLetter = "a"
longest = ""
for letter in s:
    if ord(letter) >= ord(lastLetter): 
        letters += letter
        lastLetter = letter
        if len(letters) > len(longest):
            longest = letters
    else:
        lastLetter = letter
        if len(letters) > len(longest):
            longest = letters
        letters = letter
print("Longest substring in alphabetical order is: " + longest)