# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 17:33:35 2017

@author: Nilton Junior
"""

def checkio(s):
    
    ind_lower_case_start = ord('a')
    ind_lower_case_end= ord('z')
    ind_upper_case_start = ord('A')
    ind_upper_case_end = ord('Z')
    
    size_of_list = ind_lower_case_end - ind_lower_case_start + 1
    
    freq = [0]*size_of_list

    for i in range(0,len(s)):
        
        tf = False
        
        while tf == False:
        
            j = 0    
        
            if  (   s[j] == chr(ind_lower_case_start + j)
                or  s[j] == chr(ind_upper_case_start + j)
                ):
            
                freq[j] = freq[j] + 1
                tf = True
                    
            elif j > 25:
                
                tf = True
            
            j = j + 1
        
    max_position = freq.index(max(freq))
    
    return chr(max_position + ind_lower_case_start)
            



