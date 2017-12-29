# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 08:37:42 2017

@author: Micha
"""

a="rjsfd;ljsfkgjkagjajkgkadgrovmdafdkjgakdfjg9485;lfjkdfamferm4tmukejghjrr3urjevnnvjaschsIE&(!@#498e7JpGAgaNR4T94UDJAE289493rrkgjkamf;e;gorpdc,ew,dewif"

def long_sub_string(a):
    """ returns longest substring without a repeating char"""
    L=len(a)
    k=1
    stCur=0 #index of starting position of current string
    stBest=0 #index of starting position of best string
    bestLength=1
    currentLength=1
    
    while k<L:  # for each element in a
        m=0
        
        flag=True
        curChar=a[k]
        print((m,k))
        print(a[stCur:stCur+currentLength])
        print(currentLength)
        print('-------')
        while m<currentLength and flag:
            

            if a[stCur+m]==curChar:
                flag=False
                stCur=m+1+stCur
                currentLength=currentLength-(m+1)+1
            m+=1
        if flag==True:
            currentLength+=1
        if currentLength>bestLength:
            stBest=stCur
            bestLength=currentLength
        k+=1
    bestString=a[stBest:stBest+bestLength]
    return bestString
            
    
    