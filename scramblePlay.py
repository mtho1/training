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
    
    for k in range(1,L1):  #k 1 to L1-1
        A,B,C,D = False,False,False,False
        if k<=int(0.5*L1):   # eval A and C first since they  are  smaller string which run faster
            print('eee___')
            A = is_scrambled(s1[:k],s2[:k])            
            if A==True:   # only need to check B if A is true
                B=is_scrambled(s1[k:],s2[k:])
            if (A and B) == False:
                C=  is_scrambled(s1[:k],s2[-k:])
            if (A and B)== False and C==True:  # only need to check is A and B is False 
                D=is_scrambled(s1[k:],s2[:-k])
        else: ## eval B and D first since they are smaller string which run faster
            print("fff___")
            B=is_scrambled(s1[k:],s2[k:])
            
            if B==True:
                A = is_scrambled(s1[:k],s2[:k])
            if (A and B) == False:  # only need to check is A and B is False 
                D=is_scrambled(s1[k:],s2[:-k])
            if (A and B)==False and D==True:
                C=is_scrambled(s1[:k],s2[-k:])
            
        if (A and B) or (C and D):
            return True
    return False

#s1='TinaTomStephanieMichaelTuttyNadhirahAliaLuckyLucy'
s1T='TinaTomStephanieMichaelTuttyNadhirahAliaLuckyLucy'
permInds=np.random.permutation(len(s1T))
s1="".join([s1T[permInds[k]] for k in range(0,len(s1T))])
s2=scramble(s1)
permInds=np.random.permutation(len(s1))
s3="".join([s1[permInds[k]] for k in range(0,len(s1))])

is_scrambled(s1,s2)