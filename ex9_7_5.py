#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:07:04 2019

@author: ACAN
"""
#start with lines that start with "From"
#notice that you need the text from index of @ to " " after
#creates a new file with lines needed and first " " removed
fhand = open("mbox-short.txt")
fout = open("output.txt", "w")
for line in fhand:
    if line.startswith("From"):
        x = line.find("@")
        x = int(x)
        fout.write(line[x+1:])
        
        
#opens new file, finds index loc of " "
#creates new dict with counts of email address after @        
count = {}
fhand = open("output.txt")
for line in fhand:
    x = line.find(" ")
    x = int(x)
    y = (line[:x])
    count[y] = count.get(y,0) + 1 #the get method for dictionaries
    print(count)
    
print("\n",count)        