#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 19:12:22 2019

@author: ACAN
"""
counter = 0
messages = {}
fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("From"):
        words = line.split()
        messages[words[1]] = messages.get(words[1],0) + 1
        counter += 1

print(counter)
print(messages)

largest = None
email = " "
for key,value in messages.items():
    if largest is None or value > largest:
        largest = value
        email = key
        print("\n",email, largest)
    else:
        print("\nlower than last largest", key, value)

print("\nEmail with most messages:", email, largest)    


#the below is test on reversing the key,value and saving to a diff dict
#doesn't really work because key values duplicate so there is loss
messages_reversed = {}
for key, value in messages.items():
    messages_reversed[value] = key
print("messages_reversed\n",messages_reversed)
