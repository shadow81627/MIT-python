# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 00:41:37 2016

@author: Damien Robinson
"""  
  
def reverse(L):
    """
    L: list to be reversed
    return a reversed version of the given list
    """
    result = []
    for index in range(len(L)-1, -1, -1):        
       result.append(L[index])
    return result
    
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    result = []
    for index in range(len(L)-1, -1, -1):        
       result.append(reverse(L[index]))
    L = result
