#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:24:36 2019

@author: acan
"""

score = input("Enter a score between 0.0 and 1.0:")
score = float(score)


if score < 0.0 or score >1.0:
    print("Error...you entered a value that is out of range.")
else:
    if score < 0.6:
        print('F')
    elif score < 0.7:
        print('D')
    elif score < 0.8:
        print('C')
    elif score < 0.9:
        print('B')
    else:
        print('A')
