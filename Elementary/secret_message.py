# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 17:33:35 2017

@author: Nilton Junior
"""

def checkio(text):
    
    first_letter = ord('A')
    last_letter = ord('Z')
    
    outcome = ''
    
    for i in text:
        if  (       ord(i) >= first_letter
            and     ord(i) <= last_letter
            ):
            
            outcome = outcome + i
            
    return outcome
            



