# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 08:51:27 2017

@author: Micha
"""
import math
import numpy as np
a=list(np.random.normal(size=(1000,)))
a[500]=100
a[501]=-100
def max_subarray(a,sP,endP):
    """ find the subArray of list a such that sum(a(ind1:ind2))is maximized """
    L=endP-sP
    print(L)
    if L==0:
        raise(Exception('0'))
    if L==1:
        maxSum=a[sP]
        ind1=sP
        ind2=sP+1
        return (ind1,ind2,maxSum)
    else:
        L2=math.floor(L/2)
        (ind1L,ind2L,maxSumL)=max_subarray(a,sP,sP+L2)   
        (ind1R,ind2R,maxSumR)=max_subarray(a,sP+L2,endP)
        (ind1C,ind2C,maxCross)=max_cross(a,sP,endP,sP+L2-1)   #may needs some check for length
        if maxSumL>=maxSumR and maxSumL>=maxCross:
            return (ind1L,ind2L,maxSumL)
        if maxSumR>maxSumL and maxSumR>=maxCross:
            return (ind1R,ind2R,maxSumR)
        if maxCross>maxSumR and maxCross>maxSumL:
            return (ind1C,ind2C,maxCross)
def max_cross(a,sP,endP,midP):
    """ find the subArray of list a such that sum(a(ind1:ind2))is maximized
    such that ind1<=midP AND ind2>midP"""
    temp_sum=a[midP]
    left_sum=a[midP]
    left_ind=midP
    ind_temp=midP-1
    while ind_temp>=sP:
        temp_sum+=a[ind_temp]
        if temp_sum>left_sum:
            left_sum=temp_sum
            left_ind=ind_temp
        ind_temp+=-1
    temp_sum=a[midP+1]
    right_sum=a[midP+1]
    right_ind=midP+1
    ind_temp=midP+2
    while ind_temp<endP:
        temp_sum+=a[ind_temp]
        if temp_sum>right_sum:
            right_sum=temp_sum
            right_ind=ind_temp
        ind_temp+=1
    return (left_ind,right_ind+1,right_sum+left_sum)
        
      
        
        
        
    