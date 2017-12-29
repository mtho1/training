# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:25:31 2017

@author: Micha
"""
import numpy as np

def kAndkPlus1(a,b,k):
    #find the kth and kth+1 largest value in the merged list formed from a and b
    #a and b are sorted lists
    # Do this O(log(N+M)) time
    La=len(a) #number of a values under consideration.  this will decrease as we approach a solution
    Lb=len(b) #number of a values under consideration.  this will decrease as we approach a solution
    st_a=0   #starting index of a    this will increase as we elminate possible answers
    st_b=0   #starting index of b.   this will increase as we elminate possible answers
    out=[-1,-1]
    TotalL=La+Lb  
    if k>La+Lb-1:
        raise Exception('k is too large')
    if k==La+Lb-1:  #then we know it is the largest element
        out=max(a[La-1],b[Lb-1])
        return out
    if k==0:  #then it is the smallest
        out[0]=min(a[st_a],b[st_b])
        out[1]=max(a[st_a],b[st_b])
        return out
    it=0
    
    while La>0 and Lb>0:
        #print('hi')
        it+=1
        midA=max(int(La/2)-1,0)+(st_a)
        midB=max(int(Lb/2)-1,0)+(st_b)
        T=(midA+midB)
        #print(T)
        #print(midA)
        #print(midB)
        #print(st_a+st_b)
        #print(st_a)
        #print(st_b)
        #print(a[st_a])
        #print(b[st_b])
        print(it)
        print(La)
        print(Lb)
        print(midA)
        print(midB)
        #print(st_a)
        #print(st_b)
        print('-------------')
        if k==st_a+st_b:  #then everything less than index k has been removed 
            #we know k is the smallest element
            out[0]=min(a[st_a],b[st_b])
            if La>1 and Lb>1:
                out[1]=min(min(max(a[st_a],b[st_b]),a[st_a+1]),b[st_b+1])
                return out
            elif La>1:
                out[1]=min(max(a[st_a],b[st_b]),a[st_a+1])
                return out
            elif Lb>1:
                out[1]=min(max(a[st_a],b[st_b]),b[st_b+1])
                return out
            else:
                out[1]=max(a[st_a],b[st_b])
                return out
        if T>=k:  #then we can remove some elements at the end of list from consideration
            if a[midA]>b[midB]:
                La=min(La,midA+1-(st_a))
            else:
                Lb=min(Lb,midB+1-(st_b))
        else:   # we can remove elements from start of list
            if a[midA]<b[midB]:
                La=La-(midA+1-st_a)
                st_a=midA+1
            else:
                Lb=Lb-(midB+1-st_b)
                st_b=midB+1
        if k>st_a+st_b and La>0 and Lb>0: #then we know the smallest value can be eliminated
            if a[st_a]>b[st_b]:
                st_b=st_b+1
                Lb=Lb-1
            else:
                st_a=st_a+1
                La=La-1
    if La==0:
        nRemoveA=st_a   #number of elements removed from front of listA
        out[0]=b[k-nRemoveA]
        out[1]=b[k-nRemoveA+1]
        return out
    if Lb==0:
        nRemoveB=st_b   #number of elements removed from front of listA
        out[0]=a[k-nRemoveB]
        out[1]=a[k-nRemoveB+1]
        return out
  
a=np.random.randint(low=0,high=13933393,size=(9300,))
b=np.random.randint(low=-3312433,high=13533933,size=(10000,))
c=[]
c.extend(a)
c.extend(b)
a.sort()
b.sort()
c.sort()
k=len(c)-2#int(np.random.randint(low=0,high=len(c),size=1))
y=kAndkPlus1(a,b,k)
print(y)
print(c[k:k+2])
     