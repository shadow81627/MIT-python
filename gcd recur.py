# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 01:16:58 2016

@author: Damien Robinson
"""


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)
