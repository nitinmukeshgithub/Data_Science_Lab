#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 16:37:20 2022

Given a string, find the character coming the maximum number of times in it, irrespective
of the case of the character.
Example
Input:
Pineapple
Output:
P

@author: nitin-mukesh
"""

string=(input("Enter the string "))
string=string.lower()
p_count=0
legnth=len(string)
for i in range(0,legnth,1):
    count=0
    for j in range(0,legnth,1):
        if((string[i]==string[j])):
            count+=1
            if(count>=p_count):
                p_count=count
                str=string[j]                                   
print(str)

        
             
            
            
            
            
