# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 23:55:23 2016

@author: Damien Robinson
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp > 0:
        result = base
        for i in range(0, exp - 1):
           result = result * base
        return result
    else:
        return base + 1 - base
