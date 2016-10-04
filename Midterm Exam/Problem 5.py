# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 00:35:05 2016

@author: Damien Robinson
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    returns the sum of the pairwise products of listA and listB.
    '''
    result = 0
    for index in range(len(listA)): 
        result += listA[index] * listB[index]
    return result