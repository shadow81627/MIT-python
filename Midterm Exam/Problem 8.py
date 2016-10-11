# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 02:22:21 2016

@author: Damien Robinson
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    result = 0
    for i in L:
        if len(L) < 1:
            return -1
        elif g(f(i)) == True:
            if i > result:
                result = i
        else:
            L.remove(i)
    return result