#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:05:50 2019

@author: acan
"""

list_of_numbers = []

while True:
    userinput = input("Enter a number or 'done' to quit.>> ")
    if userinput == "done":
        break
    else:
        try:
            list_of_numbers.append(float(userinput))
        except:
            print("Bad Entry")




try:
    print(list_of_numbers)
    print("Min=",min(list_of_numbers))
    print("Max=",max(list_of_numbers))
except:
    print("No numbers entered")

            