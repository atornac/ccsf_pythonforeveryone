#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:16:12 2019

@author: acan
"""

list_of_words = []
fhandle = open("romeo.txt")

for line in fhandle:
    for word in line.split():
        if word not in list_of_words:
            list_of_words.append(word)
            
print(list_of_words)
    
newlistsorted = sorted(list_of_words) 
#use sorted when you want a new list back
#t.sort would re sort the list in place but it returns none

print(newlistsorted)


newlistsorted.sort(reverse=True)
print(newlistsorted)