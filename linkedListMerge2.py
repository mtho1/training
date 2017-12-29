# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# merge 2 lists of sorted integers
a=[1,2,3,4,5,55]
b=[-3,9,4,9,9,123,-33,-55]



carryover=0

a.sort()
b.sort()
import importlib
import linkList as LL
importlib.reload(LL)
listA=LL.linkList()
listB=LL.linkList()
c=0
while c<len(a):
    listA.add(a[c])
    c+=1
c=0
while c<len(b):
    listB.add(c)
    c+=1
def merge2List2(listA,listB):
    listC=LL.linkList()
    listA.setCur(0)
    listB.setCur(0)
    listB_end=False
    listA_end=False
    while not listB_end or not listA_end:
        if (listA.cur.value>listB.cur.value or listB_end) and not listA_end:
            listC.add(listA.cur.value)
            
            if listA.cur.next != None:
                listA.nextNode()
                print(listA.cur.value)
            
            else:
                listA_end=True
        else:
            
            listC.add(listB.cur.value)
            if listB.cur.next != None:
                listB.nextNode()
                print('b')
            else:
                listB_end=True
                    
    return listC   

                  
    