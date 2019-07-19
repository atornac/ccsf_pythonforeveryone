#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:49:49 2019

@author: acan
"""

toppings = ["pepperoni", "olives", "sausage", "green peppers", "tomatoes"]

def chop(xx):
    """takes a list and deletes first and last elements"""
    del (xx[0])
    del (xx[-1])
    return None


print(toppings, "before chop")
chop(toppings)
print(toppings, "after chop")


cars = ["triumph", "celica", "van", "civic", "nissan", "highlander", "bmw"]



#both methods work...wonder which one if more pythonic
def middle(yy):
    """takes list, removes first and last elements, creates new list"""
    zz = list()
    for item in yy[1:-1]:
        zz.append(item)
    print(zz)
    
print(cars)    
middle(cars)
    

def middle2(yy):
    "takes list, removes first and last elements"""
    return yy[1:-1]
    
    
zzz = middle2(cars)
print(zzz)