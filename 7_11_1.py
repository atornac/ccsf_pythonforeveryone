#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:17:57 2019

@author: acan
"""

fhand = open("mbox-short.txt")
for line in fhand:
    print(line.upper().rstrip())
    

