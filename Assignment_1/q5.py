#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 21:51:28 2022

Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. For a
given n write a program to compute factorials of numbers from 1 to n and print it in the
following manner (example when n=4).
4! = 24
3! = 6
2! = 2

@author: nitin-mukesh
"""
num=int(input("Enter the number for factorial "))
product=1
count=1
for i in range(num,1,-1):
    product*=i
for num in range(num,1,-1):      
    print(num,"!=",product/count)
    count*=num

