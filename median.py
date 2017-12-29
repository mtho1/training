# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:11:37 2017

@author: Micha
"""

#median of 2 sorted lists.  should run in O(log(N +M)) where N and M are the sequene lenghts

                                           
import numpy as np  
import math                                        
a=np.random.uniform(size=(10,)).tolist()
a.sort()
b=np.random.uniform(size=(11,)).tolist()
b.sort()


def medianSort(a):
    #find median of sorted array
    L=len(a)
    if L%2==1:
        medianVal=a[math.floor(L/2)]
    else:
        medianVal=( a[round(L/2)]+a[round(L/2)-1])*0.5
    return medianVal
def medianSortSkewed(a,skew):
    #find median of sorted array with offset
    #skew >=1 back loaded
    #skew=<=-1 front loaded
    L=len(a)+abs(skew)
    if L%2==1:
        if skew>=1:
            medianVal=a[math.floor(L/2)]
        else:
            medianVal=a[math.floor(L/2)+skew]
    else:
        if skew>=1:
            medianVal=( a[round(L/2)]+a[round(L/2)-1])*0.5
        else:
            medianVal=( a[round(L/2)+skew]+a[round(L/2)-1+skew])*0.5
    return medianVal


def median2Sort(a,b):
    #find median of the merge of 2 sorted lists
    La=len(a)
    Lb=len(b)
    if La>Lb:
        raise Exception('lenA<=lenB required')
    if La==1 and Lb==1:
        return 0.5*(La+Lb)
    if La==1 and a[0]<medianSort(b):
        return medianSortSkewed(b,-1)
    if La==1 and a[0]>medianSort(b):
        return medianSortSkewed(b,+1)
    if La==1 and a[0]==medianSort(b):
        return a
    if La==2 and Lb==2:
        return ( max([a[0],b[0]])+min([a[1],b[1]]))*0.5
    
    if La==2 and Lb >=4
        temp=0
        for k in [0,1]:
            if a[k]<=medianSort(b):
                temp-=1
            else:
                temp+=1
        if temp!=0:
            return medianSortSkewed(b,temp)
        else:
            return medianSort(b)
    
    flag=False
    while flag==False:
        La=len(A)
        Lb=len(B)
        Ma=medianSort(a)
        Mb=medianSort(b)
        remove=floor(La/2)-1
        if Ma<Mb:
            a=a[remove:]
            b=b[:-remove]
        elif Ma>Mb:
            a=a[:-remove]
            b=b[remove:]
                         
                         
            
            
    
    
    
    
    