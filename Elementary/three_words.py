# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 17:33:35 2017

@author: Nilton Junior
"""

def checkio(words):
    
    tf = False
    count = 0
    split_text = words.split(" ")
    
    for i in split_text:
        
        if  (   (       ord(i[0]) >= ord('a')
                and     ord(i[0]) <= ord('z')
                )
            or  (       ord(i[0]) >= ord('A')
                and     ord(i[0]) <= ord('Z')
                ) 
            ):
            count = count + 1
            if count >= 3:
                tf = True
                break
        else:
            count = 0
                
    return tf
            



