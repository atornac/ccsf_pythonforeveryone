#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 12:43:09 2019

@author: acan
"""

wordsdict = {}

fhandle = open("words.txt")

for line in fhandle:
    words = line.split() #words is a list, elements are the words in the line
    print(words)
    for word in words:
        wordsdict[word] = " "
            
        
print(wordsdict)    
print(len(wordsdict))


x = ("for" in wordsdict)
print(x)

fhandle.close()




print("Test 1")
#example using dictionary as counter
#a counter of how many times a letter appears in the word
#not a counter of how many letters in the word
word2 = "brontosaurus"

d = dict()
for c in word2:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
        
print(d)


print("Test 2")
#a more succinct way
dd = dict()
for c in word2:
    dd[c] = dd.get(c,0) + 1
print(dd)
#this works because there are no values for the keys...so it all starts at 0

