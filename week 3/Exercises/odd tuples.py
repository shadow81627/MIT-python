# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 23:08:52 2016

@author: Damien Robinson
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    bTup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            bTup += (aTup[i],)
    return bTup