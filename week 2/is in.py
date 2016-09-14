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
    
    if aStr == '':
        return False
    #Base case to test if middle character in aStr and char are the smae
    elif char == aStr[middle]:
        return aStr == char
    #Test if char is smaller than middle 
    elif char < aStr[middle]:
        isIn(char, aStr[:middle])
    #Test if char is bigger than middle
    elif char > aStr[middle]:
         isIn(char, aStr[middle+1:])
    #return False if we could not find the char in aStr
    else:
        return False