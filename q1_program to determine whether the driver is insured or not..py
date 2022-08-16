#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 15:47:45 2022

A company insures its drivers in the following cases:
- If the driver is unmarried.
- If the driver is married, above 45 years of age and has at least two children.
- If the driver is married, above 35 years of age and has at least one child.
In all the other cases, the driver is not insured.
If the marital status, age and number of children of the driver are the inputs, Write a
program to determine whether the driver is insured or not.


@author: nitin-mukesh
"""

marital=input(("Enter the marital status(married/unmarried) "))

if(marital=="unmarried"):
    print("Provide the insurance to the driver ")
else:
    age,childrens=int(input("Enter the age ")),int(input("Enter the no. of Childrens "))
    if(age>45 and childrens>=2):
        print("Provide the insurance to the driver ")
    elif(age>35 and childrens>=1):
        print("Provide the insurance to the driver ")
    else:
        print("Don't provide the insurance to the driver ")
    









