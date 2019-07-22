#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 08:50:46 2019

@author: ACAN
"""

import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')

fhand = open('cover3.jpg', 'wb')
size = 0

while True:
    info = img.read(100000)
    if len(info) < 1: break 
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()