#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:23:54 2019

@author: acan
"""

#open the file with handle

fhandle = open('mbox-short.txt')

for line in fhandle:
    if line.startswith("From"):
        x = line.split()
        if len(x) > 3:
            print(line.rstrip())
            print(x[2],"\n")


