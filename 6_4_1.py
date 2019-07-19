#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:12:57 2019

@author: acan
"""

index = -1

word = "Fruit"

nbr_of_letters = len(word)
indexmax = -1*(nbr_of_letters)

while index >= indexmax:
    print(word[index])
    index = index - 1


print("or another method")

print(word[::-1])

print(word[:])


x = list(word)

print(x)