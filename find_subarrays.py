# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 09:19:48 2018

@author: Micha
"""

def find_subarrays(a,x):
    #find all subarrays of a ,q, where sum(q) = x
    L=len(a)
    for q in range(0,L):
       # print(x)
       # print(a)
       # print(q)
       # print('-----')
        if a[q]==x:
            print(x)
            print(a[q])
            print('------')
            return list([q])
        elif L>1:
            dropped=a[q]
            a.pop(q)
            sub=find_subarrays(a,x-dropped)
            a.insert(q,dropped)
            if sub !=-1:
                #need to redefine sub
                for v in range(0,len(sub)):
                    if sub[v]>=q:
                        sub[v]+=1
                sub.extend([q])
                print(x)
                print([a[v] for v in sub])  
                print('------')
                return sub  
    return -1
def find_subarrays2(a,x):
    #find all subarrays of a ,q, where sum(q) = x
    L=len(a)
    for q in range(0,L):
        #print(x)
        #print(a)
        #print(q)
        #print('-----')
        if a[q]==x:
           # print(x)
           # print(a[q])
           # print('------')
            yield list([q])
        elif L>1:
            dropped=a[q]
            dropFlag=True
            b=a.copy()
            b.pop(q)
            for sub in find_subarrays2(b,x-dropped):
                
                if type(sub)==list:
                    
                    #need to redefine sub
                    for v in range(0,len(sub)):
                        if sub[v]>=q:
                            sub[v]+=1
                    sub.extend([q])
                           # print(x)
                           # print([a[v] for v in sub])  
                           # print('------')
                    yield sub                      
    yield -1           
def find_subarrays3(a,x):
    #find all subarrays of a ,q, where sum(q) = x
    L=len(a)
    for q in range(0,L):
        #print(x)
        #print(a)
        #print(q)
        #print('-----')
        if a[q]==x:
           # print(x)
           # print(a[q])
           # print('------')
            yield list([q])
            dropFlag=False
        elif L>1:
            dropped=a[q]
            dropFlag=True
            a.pop(q)
            #b=a.copy()
            #b.pop(q)
            
            
            for sub in find_subarrays3(a,x-dropped):
                
                if type(sub)==list:
                    
                    #need to redefine sub
                    for v in range(0,len(sub)):
                        if sub[v]>=q:
                            sub[v]+=1
                    sub.extend([q])
                           # print(x)
                           # print([a[v] for v in sub])  
                           # print('------')
                    a.insert(q,dropped)
                    yield sub
                    a.pop(q)
            a.insert(q,dropped)                      
    yield -1
def find_subarrays4(a,x):
    #find all subarrays of a ,q, where sum(q) = x
    L=len(a)
    #print(L)
    #print(a)
    if L==1:
        if a[0]==x:
            yield list([0])
        else:
            yield -1
    for q in range(0,L):
        #print(x)
      #  print('---------')
      #  print(a)
      #  print(q)
      #  print(L)
      #  print('-----')
        if a[q]==x:
           # print(x)
           # print(a[q])
           # print('------')
            yield list([q])
            dropFlag=False
        elif L>1:
            dropped=a[q]
            dropFlag=True
            #a.pop(q)
            #b=a.copy()
            #b.pop(q)
          #  print("=========")
         #   print(q)
         #   print(a)
            
            allDropped=a[:q+1]
            a=a[q+1:]  # all cases for 1:q-1 have been covered so we can omit. we assume a[q] is in the set already
           # print(a)
           # print(allDropped)
           # print("========")
            for sub in find_subarrays4(a,x-dropped): # minus dropped since we assume a[q] is in the set
                
                if type(sub)==list:
                    
                    #need to redefine sub
                    for v in range(0,len(sub)):
                        sub[v]+=q+1
                    sub.extend([q])
                           # print(x)
                           # print([a[v] for v in sub])  
                           # print('------')
                    #a.insert(q,dropped)
                    for vv in allDropped:
                        a.insert(0,vv)
                    yield sub
                    a=a[q+1:]
                   # print("!!!!!!!!!!!!")
                   # print(q)
                   # print(a)
                   # print(allDropped)
                   # print("!!!!!!!!!!!")
            for vv in allDropped:
                a.insert(0,vv)                      
    yield -1     
def find_subarrays5(a,x,st=0):
    #find all subarrays of a[st:] ,q, where sum(q) = x
    lenA=len(a)
    L=lenA-st
    #print(L)
    #print(a)
    if L==1:
        if a[st]==x:
            yield list([0])
        else:
            yield -1
    for q in range(st,lenA):
        #print(x)
      #  print('---------')
      #  print(a)
      #  print(q)
      #  print(L)
      #  print('-----')
        if a[q]==x:
           # print(x)
           # print(a[q])
           # print('------')
            yield list([q])
            dropFlag=False
        elif L>1:
            dropped=a[q]
          #  dropFlag=True
            #a.pop(q)
            #b=a.copy()
            #b.pop(q)
          #  print("=========")
         #   print(q)
         #   print(a)
            
           # allDropped=a[:q+1]
           # a=a[q+1:]  # all cases for 1:q-1 have been covered so we can omit. we assume a[q] is in the set already
           # print(a)
           # print(allDropped)
           # print("========")
            for sub in find_subarrays5(a,x-dropped,q+1): # minus dropped since we assume a[q] is in the set.# all cases for 1:q-1 have been covered so we can omit. we assume a[q] is in the set already
                
                if type(sub)==list:
                    
                    #need to redefine sub
                    sub.extend([q])   # recall we assume q is in the set
                           # print(x)
                           # print([a[v] for v in sub])  
                           # print('------')
                    #a.insert(q,dropped)
                    yield sub
                  
                   # print("!!!!!!!!!!!!")
                   # print(q)
                   # print(a)
                   # print(allDropped)
                   # print("!!!!!!!!!!!")
    return     