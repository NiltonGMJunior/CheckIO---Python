# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 17:33:35 2017

@author: Nilton Junior
"""

def checkio(number):
    
    if number % 3 == 0:
        if number % 5 == 0:
            number = "Fizz Buzz"
        else:
            number = "Fizz"
    elif number % 5 == 0:
        number = "Buzz"
                
    return str(number)
            



