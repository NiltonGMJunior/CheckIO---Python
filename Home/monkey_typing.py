# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 17:12:39 2017

@author: Nilton Junior
"""

def count_words(text, words):
    
    text = text.lower()
    
    count = 0
    
    for i in words:
        ind = 0
        while test != -1:
            test = text.find(i, ind)
            if test != -1:
                ind = test + 1
                count += 1
    
    return count