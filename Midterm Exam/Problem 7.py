# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 01:45:40 2016

@author: Damien Robinson
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}
    difference = {}
    
    for key in d1.keys():
        if key in d2.keys():
          intersect[key] = f(d1[key], d2[key])
        else:
            difference[key] = d1[key]
            
    for key in d2.keys():
        if key in d1.keys():
          intersect[key] = f(d1[key], d2[key])
        else:
            difference[key] = d2[key]
    return (intersect, difference)