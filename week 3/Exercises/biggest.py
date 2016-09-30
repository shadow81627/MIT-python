# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:37:49 2016

@author: Damien Robinson
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = {'lenght': 0}
    for key in aDict.keys():
        if len(aDict[key]) > result['lenght']:
            result['key'] = key
            result['lenght'] = len(aDict[key])
    return result['key']