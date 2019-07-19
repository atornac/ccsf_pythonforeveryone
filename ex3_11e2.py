#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:07:41 2019

@author: acan
"""
try:
    HOURS = input("Enter hours:")
    RATE = input("Enter rate:")
    HOURS = float(HOURS)
    RATE = float(RATE)
    OT_PAY = (HOURS - 40) * 1.5 * RATE
    REG_PAY = HOURS * RATE
    if HOURS > 40:
        REG_PAY = 40*RATE
        TOTALPAY = REG_PAY + OT_PAY
        print("Pay with overtime = ", TOTALPAY)
    else:
        TOTALPAY = HOURS * RATE
        print("Pay NO overtime = ", TOTALPAY)
except ValueError:
    print("Numbers only please.")
