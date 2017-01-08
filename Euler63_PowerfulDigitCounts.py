#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 21:02:12 2017

@author: christophergreen

Powerful digit counts
Problem 63
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 
134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

import math;

def find_powerfuls(numdig):
    start='1'+('0'*(numdig-1));
    end='9'*numdig;
    print("for number of digits",numdig,"the start and end values are:",start,"and",end);
    first=math.ceil((int(start)**(1/numdig)))
    last=math.ceil((int(end)**(1/numdig))-.3) #to deal with weird rounding issues for higher powers
    print("first and last are:",first,"and",last);
    print("this is the",last-first,"items:");
    for i in range(first,last):
        print(i,"to the power",numdig,"=",i**numdig,"is in this range");
    print("");
    return (last-first);

    
def count_all_powerfuls():
    print("");
    print("we start off with powercount being 9 to account for the ints 1 through 9 to the first power");
    print("");
    powercount=9 #to account for the ints from 1 through 9 to the first power
    i=2;
    while True:
        holder=find_powerfuls(i);
        if holder==0:
            break;
        else:
            powercount+=holder
        i+=1;
    print("the total number of powerfuls is",powercount);
    return powercount;
    
count_all_powerfuls(); #-->the total number of powerfuls is 49 CORRECT
    