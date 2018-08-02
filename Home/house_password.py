# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:12:19 2017

@author: Nilton Junior
"""

def checkio(password):
    
    tf1, tf2, tf3 = 0, 0, 0
    
    for i in password:
        if i.isdigit():
            tf1 = 1
        elif i.lower() == i:
            tf2 = 1
        elif i.upper() == i:
            tf3 = 1
        
    return tf1*tf2*tf3*(len(password) >= 10)