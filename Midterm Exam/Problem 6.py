# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 00:41:37 2016

@author: Damien Robinson
"""  
    
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """

    for index in range(len(L)-1, -1, -1):
       L[index].reverse()
    L.reverse()