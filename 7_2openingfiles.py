#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:19:09 2019

@author: acan
"""
#opening a file and counting lines
#\n...the newline character ends every line
fhand = open("mbox.txt")
count = 0
for line in fhand:
    count +=1
print("Line Count:", count)


#opening a file and reading the contents
fhand = open("mbox.txt")
inp = fhand.read()
print(len(inp))
print((inp[:20]))

#searchin through a file

fhand = open("mbox.txt")
count = 0
for line in fhand:
    line = line.rstrip() #optional - removes \n so no additional line
    if line.startswith("From:"):
        count += 1
        print(line)
        
print(count)

#searching for a specific set of text in a line
fhand = open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue  #-1 is result if no find
    print(line)
    
    
#using try except
    
fname = input("Enter file name:")
try:
    fhand = open(fname)
    count = 0
    for line in fhand:
        if line.startswith("Subject:"):
            count +=1
    print("There were", count, "subject lines in", fname)
except:
    print("file name entered not found")



