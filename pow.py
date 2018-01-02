# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 23:16:50 2017

@author: Micha
"""
import math
def powMike(x,n):
    #take x to the n-th power. n is integer
    print(n)
    if n<=1:
        return x
    else:
        N2=math.floor(n/2.0)
        xN2=powMike(x,N2)
        
        if N2*2<n:
            return (xN2*xN2*x)
        else:
            return xN2**2
    