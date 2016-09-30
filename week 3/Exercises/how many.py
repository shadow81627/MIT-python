# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:37:49 2016

@author: Damien Robinson
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    num = 0
    for key in aDict.keys():
        num += len(aDict[key])
    return num