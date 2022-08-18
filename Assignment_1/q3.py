#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 16:32:12 2022

Given a year as input, print if it is leap year or not.

@author: nitin-mukesh
"""

year=int(input("Enter the year to check for leap year "))

if(year%400==0):
    print("The given year",year," is a leap year")
elif(year%4==0 and year%100!=0):
        print("The given year",year," is a leap year")    
else:
    print("The given year",year," is not a leap year")