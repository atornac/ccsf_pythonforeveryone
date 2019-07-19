#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:40:50 2019

@author: acan
"""

def count(string, letter):
    """counts the number of letters in a string"""
    word = string
    count = 0
    for alphabet in word:
        if letter == alphabet:
            count = count + 1
    print("There are", count, letter+"'s", "in the word", string + ".")
    

count('banana','a')


#also use the string method 'count'

string = 'banana'
how_many_a = string.count('a')
print(how_many_a)