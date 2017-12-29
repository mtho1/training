# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# create two list representing a number in reverse order.   LSD is first element of list
# Add the two numbers
a=[1,2,3,4,5]
b=[3,9,4,9,9]
c=[]

carryover=0



while len(a)>0 and len(b)>0:
    temp=a.pop(0)+b.pop(0)+carryover
    if temp>9:
        carryover=1
        temp=temp-10
    else:
        carryover=0
    c.append(temp)
while len(a)>0:
    temp=a.pop(0)+carryover
    if temp>9:
        carryover=1
        temp=temp-10
    else:
        carryover=0
    c.append(temp)
while len(b)>0:
    temp=b.pop(0)+carryover
    if temp>9:
        carryover=1
        temp=temp-10
    else:
        carryover=0
    c.append(temp)
if carryover>0:
    c.append(carryover)
          
                  
    