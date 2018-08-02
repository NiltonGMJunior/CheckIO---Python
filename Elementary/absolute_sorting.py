# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 14:02:29 2017

@author: Nilton Junior
"""

def checkio(numbers_array):
    
    sorted_array = list(numbers_array) # This converts the input argument to a list
    
    swap_condition = True # Flags the occurence of a swap
    
    while swap_condition: # Loops through array while changes are being made
        swap_condition = False # Resets swap condition
        for i in range(len(sorted_array) - 1): # Runs through pairs of adjacent elements in the array
            if abs(sorted_array[i]) > abs(sorted_array[i + 1]):
                temp = sorted_array[i]
                sorted_array[i] = sorted_array[i + 1]
                sorted_array[i + 1] = temp
                swap_condition = True
            
    return sorted_array