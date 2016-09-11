# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 00:15:23 2016

@author: Damien Robinson
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return base + 1 - base
    else:
        return base * recurPower(base, exp - 1)
