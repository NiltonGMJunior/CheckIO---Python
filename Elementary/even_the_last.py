# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 17:33:35 2017

@author: Nilton Junior
"""

def checkio(u):
    
    if len(u) == 0:
        outcome = 0       
    else:   
        last_element = u[len(u) - 1]   
        v = u[0:len(u):2]
        outcome = last_element*sum(v)
    
    return outcome
            



