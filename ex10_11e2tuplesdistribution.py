#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:09:29 2019

@author: acan

Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
"""

hours = {}
counter = 1
fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("From") and "2008" in line:
        print(line.rstrip())
        line.strip("\n")
        x = line[-14:-1]
        y = x[:2]
        print(x)
        print(counter,"***\n")
        hours[y] = hours.get(y,0) + 1
        counter +=1


print(hours)
for key, value in hours.items():
    print(key,value)
    
zzz = list(hours.items())
zzz.sort()
print(zzz)
for key, item in zzz:
    print(key, item)
#done
    
#alternate method
