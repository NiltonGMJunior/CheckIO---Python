# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:00:37 2017

@author: Nilton Junior
"""
    
def checkio(data):
    
    non_unique_array = []
    
    for i in data:
        if not(isUnique(data, i)):
            non_unique_array.append(i)
            
    return non_unique_array

def isUnique(data, element):
    
    if type(element) == str:
        cnt = data.count(element.lower()) + data.count(element.upper())
    else:
        cnt = data.count(element)
    
    return cnt == 1
