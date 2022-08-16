#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 22:19:30 2022

Write a program to print the following pascal triangle pattern given its height as input -
   1
  1 1
 1 2 1
1 3 3 1
1 4 6 4 1

@author: nitin-mukesh
"""
import math
row=0
height=int(input("Enter the height of the Pascal Traingle:"))

for n in range(0,height,1):
    print("")
    count=0
    for r in range(0,n+1,1):
        if(count!=1):
            for space in range(height-n,0,-1):           
                print(" ",end="")
                count=1
        ans=(math.factorial(n))/((math.factorial(r))*(math.factorial(n-r)))    
        print(int(ans),end="")
        print(" ",end="")
        
