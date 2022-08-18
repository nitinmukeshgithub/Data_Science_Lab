#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 22:14:43 2022

Write a program to check whether a given number is odd or even using bitwise
operators.

@author: nitin-mukesh
"""
num=input("Enter the number to check for odd or even")

if((int(num)&1)==1):
    print("the number is odd")
else:
    print("the number is even")


