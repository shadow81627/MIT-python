# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 02:07:29 2016

@author: Robinson
"""
s = 'azcbobobegghakl'
numBob = 0
letters = ""
search = "bob"
   
for i in range(len(s)):
    letters = s[i: i+3]
    if letters == search:
        numBob += 1
print("Number of times bob occurs is: " + str(numBob))