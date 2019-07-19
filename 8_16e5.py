#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:47:14 2019

@author: acan
"""

fhandle = open(input("Enter file name:>>"))

count = 0
for line in fhandle:
    if line.startswith("From"):
        x = line.split()
        if len(x)> 2:
            print(x[1])
            count +=1

print(count)
