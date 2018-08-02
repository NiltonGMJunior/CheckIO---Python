# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 17:33:35 2017

@author: Nilton Junior
"""

def checkio(*args):
    
    if len(args) == 0:
        outcome = 0
    else:
        outcome = max(args) - min(args)
                
    return outcome
            



