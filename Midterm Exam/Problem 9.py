# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 03:05:23 2016

@author: Damien Robinson
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    for i in range(len(aList)):
        if type(aList[i]) is list:
            return flatten(aList[i])
        else:
            return aList
    
aList = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(aList))