# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:08:22 2016

@author: Robinson
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    #Find and store the middle point of aStr
    middle = len(aStr) // 2
    
    #aStr has 1 or None elements
    if len(aStr) < 1:
        return aStr == char
    #Base case to test if middle character in aStr and char are the smae
    elif char == aStr[middle]:
        return aStr[middle] == char
    #char is smaller than middle 
    elif char < aStr[middle]:
        return isIn(char, aStr[:middle])
    #char is bigger than middle
    else:
         return isIn(char, aStr[middle + 1:])