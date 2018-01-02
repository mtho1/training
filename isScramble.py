# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 21:49:12 2017

@author: Micha
"""

class Solution(object):
    def isScramble(self,s1,s2):
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
                
                A = self.isScramble(s1[:k],s2[:k])            
                if A==True:   # only need to check B if A is true
                    B=self.isScramble(s1[k:],s2[k:])
                if (A and B) == False:
                    C=  self.isScramble(s1[:k],s2[-k:])
                if (A and B)== False and C==True:  # only need to check is A and B is False 
                    D=self.isScramble(s1[k:],s2[:-k])
            else: ## eval B and D first since they are smaller string which run faster
            
                B=self.isScramble(s1[k:],s2[k:])
            
                if B==True:
                    A = self.isScramble(s1[:k],s2[:k])
                if (A and B) == False:  # only need to check is A and B is False 
                    D=self.isScramble(s1[k:],s2[:-k])
                if (A and B)==False and D==True:
                    C=self.isScramble(s1[:k],s2[-k:])
            
            if (A and B) or (C and D):
                return True
        return False