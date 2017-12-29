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
import linkList2 as LL
importlib.reload(LL)
listA=LL.linkList2()
listB=LL.linkList2()
c=0
while c<len(a):
    listA.add(a[c])
    c+=1
c=0
while c<len(b):
    listB.add(c)
    c+=1
def merge2List2(listA,listB):
    listC=LL.linkList2()
    listA.setCur(0)
    listB.setCur(0)
    listB_end=False
    listA_end=False
    while not listB_end or not listA_end:
        if (listA.cur.element()>listB.cur.element() or listB_end) and not listA_end:
            listC.add(listA.cur.element())
            
            if listA.cur.has_next():
                listA.nextNode()
                print(listA.cur.element())
            
            else:
                listA_end=True
        else:
            
            listC.add(listB.cur.element())
            if listB.cur.has_next():
                listB.nextNode()
                print('b')
            else:
                listB_end=True
                    
    return listC   

                  
    