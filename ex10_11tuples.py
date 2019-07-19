#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:56:56 2019

@author: acan
"""
"""
Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the num-
ber of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.
"""

addresses = {}

fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("From"):
        x = line.find(" ")
        y = x+1 #index number signify space before address
        newline = line[y:]
        z = newline.find(" ")
        address = newline[:z]
        addresses[address] = addresses.get(address,0) + 1
print("Follows: dict with count per person of email.")        
print(addresses,"\n")



#address_list = list(addresses.items())
#an amazing method for disctionaries...got to remember this
#but since I need value, key pairs instead of key,value the 
#other way actually works best


"""
i originally generate the list of tuples per below
but the above is mo betta
"""

address_list = []
for key, value in addresses.items():
    tup = value,key
    address_list.append(tup)


print("Following: list of tuples count per person to email address")
print(address_list)

address_list.sort(reverse=True)
print("List sorted in reverse order:\n", address_list, "\n")

print(max(address_list))



