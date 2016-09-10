# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 01:54:35 2016

@author: Robinson
"""
s = 'azcbobobegghakl'
numVowels = 0
for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        numVowels += 1
print("Number of vowels: " + str(numVowels))