# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 00:37:18 2016

@author: Damien Robinson
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    divisor = a
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            divisor = i
    return divisor
            