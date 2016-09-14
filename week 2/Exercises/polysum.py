# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:08:37 2016

@author: Damien Robinson
"""

from math import *

def polysum(n, s):
    '''
    n: number of sides
    s: side length
    
    returns: sum  of the area and square of the perimeter of the regular 
    polygon rounded to 4 decimal places.
    '''
    #calculate area of the polygon
    area = 0.25 * n * s ** 2 / tan(pi / n)
    
    #calculate perimeter of the polygon then square it
    perimeter = (s * n) ** 2
    
    #sum of perimeter and area
    sum = area + perimeter
    
    return round(sum, 4)
