# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:19:28 2023

@author: avina
"""

def find_common(str1,str2):
    common=''
    min_len = min(len(str1), len(str2))
    for i in range (1, min_len+1):
        if str1[-i:] == str2[:i]:
            common = str1[-i:]
        return common
    
def join_strings(words):
    result = words[0]
    for i in range(1,len(words)):
        common = find_common(result,words[i])
        result += words[i][len(common):]
    return result

num_words = int(input("Enter the Number of Words: "))
input_words = [input(f"Enter word {i+1}: ") for i in range(num_words)]
    
output = join_strings(input_words)
print("Output: ",output)
        
    
    
