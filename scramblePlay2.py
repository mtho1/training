# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:11:55 2017

@author: Micha
"""
import numpy as np


def scramble(s):
    L=len(s)
    if L==1:
        return s
    
    k=np.random.randint(low=1,high=L)   #uniform int from 1 to L-1 
    flip=np.random.binomial(1,0.5)
    if flip==1:
        return scramble(s[k:L])+scramble(s[0:k])
    else:
        return scramble(s[0:k])+scramble(s[k:L])
it=0    
def is_scrambled(s1,s2):
    raise(Exception('wrong'))
    global it
    it+=1
    print(it)
    L1=len(s1)
    L2=len(s2)
    if L1  != L2:
        return False
    if s1==s2:
        return True
    if sorted(s1) != sorted(s2):
        return False
    if L1<=4:
        return sorted(s1)==sorted(s2)
    
    for k in range(1,L1):  #k 1 to L1-1
        A,B,C,D = False,False,False,False
        print('eee')
        A = is_scrambled(s1[:k],s2[:k])
        B=is_scrambled(s1[k:],s2[k:])
        D=is_scrambled(s1[k:],s2[:-k])
        C=is_scrambled(s1[:k],s2[-k:])
        if (A and B) or (C and D):
            return True
    return False

s1='TinaTomStephanieMichaelTuttyNadhirahAliaLuckyLucy'
s2=scramble(s1)
permInds=np.random.permutation(len(s1))
s3="".join([s1[permInds[k]] for k in range(0,len(s1))])

is_scrambled(s1,s2)