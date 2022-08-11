#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:04:59 2022

@author: nitin-mukesh
"""
n1,n2,n3=int(input("Enter the first number")),int(input("/n Enter the second number")),int(input("Enter the third number"))
if(n1>n2):
    print("")
elif(n1>n3):
    print(n1,"is the largest number")
elif(n3>n1):
    print(n3,"is the largest number")
else:
    if(n2>n3):
        print(n2,"is the largest number")
    else:
        print(n3,"is the largest number")