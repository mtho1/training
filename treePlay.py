# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 15:58:20 2017

@author: Micha
"""
import importlib
import linked_binary_tree
importlib.reload(linked_binary_tree)

MikeTree=linked_binary_tree.LinkedBinaryTree()

#rootPosition=MikeTree._add_root(4)

aList=[1,54,20,54,21,11,90,-4,-5,23,95,32]

def addToTree(tree,theList,st,pos=None):
    #add elements of theList to tree such that tree is complete
    #places theList[st] in left child of pos
    #places theList[st+1] in right child of pos
    #this goes depth first
    L=len(theList)
    if st==0 or pos == None:
        print('a')
        posNew=tree._add_root(theList[st])
        addToTree(tree,theList,2*(st+1)-1,posNew)
    elif st<L:
        
              #print(L)
        print(st)
        print('---------')
        posL=tree._add_left(pos, theList[st])
        addToTree(tree,theList,2*(st+1)-1,posL)
        if st+1<L:
            print('c')
            #print(L)
            print(st+1)
            print('---------')
            posR=tree._add_right(pos,theList[st+1])
            addToTree(tree,theList,2*((st+1)+1)-1,posR)
    return
def addToTree2(tree,theList):
    #add elements of theList to tree such that tree is complete
    #this goes breadth first and doesn't use recurrsion
    L=len(theList)
    list_of_adds=[]   #list of positions that will be given a value 
    list_of_adds=[tree._add_root(None)]   
    st=0
    while len(list_of_adds)>0:
        pos=list_of_adds.pop(0)
        tree._replace(pos,theList[st])  #set value
        if 2*(st+1)-1 <L:   #add a left node
            list_of_adds.append(tree._add_left(pos, None))
        if 2*((st+1))<L:
            list_of_adds.append(tree._add_right(pos, None))
        st=st+1
    return
            
        
    
    
    
  
    
    
        
