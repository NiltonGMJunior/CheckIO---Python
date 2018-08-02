# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:29:23 2017

@author: Nilton Junior
"""

def index_power(array, n):
    
    if n > len(array) - 1:        
        return -1    
    else:
        return array[n]**n