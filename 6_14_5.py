#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:49:34 2019

@author: acan
"""

str = "X-DSPAM-Confidence:0.8475"

colon_location = str.find(":")

print("colon index number =",colon_location)

extract = str[colon_location+1:] #want to start slice AFTER the colon

print(extract)
print(type(extract)) #verifying type

extract_converted = float(extract) #changing type
print(extract_converted)

#6_14_6

y = str.replace('e','$')
print(y)