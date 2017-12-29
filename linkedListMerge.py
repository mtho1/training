# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# merge 2 lists of sorted integers
a=[1,2,3,4,5,55]
b=[-3,9,4,9,9]


carryover=0

a.sort()
b.sort()

def merge2Lists(a,b):
    c=[]
    if len(b)>0:
            btemp=b.pop(0)
    while len(a)>0:              
        flag=True
        atemp=a.pop(0)
        while len(b)>0 and flag:
            print(atemp)
            print(btemp)
            print('-----')
            if atemp>btemp:
                c.append(btemp)
                btemp=b.pop(0)
            else:
                c.append(atemp)
                flag=False
        if flag:   #then we went through b without finding anything > atemp
                c.append(atemp)
    
    while len(b)>0:
             btemp=b.pop(0)
             c.append(btemp)
    return c
                  
    