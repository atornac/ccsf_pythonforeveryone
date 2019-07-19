#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:25:14 2019

@author: acan


Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).
"""


days={}

file = input("Enter file name:>>")
fhand = open(file)
for line in fhand:
    if line.startswith("From"):
        words = line.split()
        if len(words) > 3:
            days[words[2]] = days.get(words[2],0) + 1
            
            


print(days)    