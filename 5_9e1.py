#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 07:42:26 2019

@author: acan
"""

"""pseudocode
ask user to input numbers
continue asking until user enters "done"
print out the total, count and average of the numbers
if user enters non-number, use try except to print error
skip to next number


"""
numbers = []

while True:
    userinput = input("Enter a number.\n(Enter 'done' to quit.) > ")
    if userinput == "done":
        print("\nThanks...smell you later.")
        break
    try:
        number = float(userinput)
        numbers.append(number)
    except:
        print("Oops, you entered bad data.")

print("List of numbers:", numbers)
print("There were", len(numbers),"numbers provided.")
print("Avg of numbers", sum(numbers)/len(numbers))
print("Max value in the list is:", max(numbers))
print("Min value in the list is:", min(numbers))


#how do you do above without min, max and list

