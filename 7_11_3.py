#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:58:49 2019

@author: acan
"""

while True:
    filename = input("Enter file name or q to quit:")
    if filename == "na na boo boo":
        print("Easter egg time")
        break
    elif filename == 'q':
        break
    else:
        spam_confidence = []
        spam_confidence_float = []
        try:
            fhand2 = open(filename) #fhand is the handle for the open file
            for line in fhand2:
                if line.find("X-DSPAM-Confidence") == -1: #means did not find
                    continue
                else:
                    index = line.find(":")+1
                    spam_confidence.append(line[index:-1])
            for x in spam_confidence:
                spam_confidence_float.append(float(x))
            print(spam_confidence)
            print(spam_confidence_float)
            average_scf = sum(spam_confidence_float)/len(spam_confidence_float)
            print (average_scf)
        except:
            print("bad file name")
    