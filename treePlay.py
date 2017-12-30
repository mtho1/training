# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 15:58:20 2017

@author: Micha
"""
import importlib
import linked_binary_tree
import math

importlib.reload(linked_binary_tree)

MikeTree=linked_binary_tree.LinkedBinaryTree()

#rootPosition=MikeTree._add_root(4)

aList=list(np.random.normal(size=(100,)))

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
            
        
def max_heapify(tree,pos):
    #list_pos=tree.breadthfirst_array()
    #L=len(list_pos)
    LeftNode = MikeTree.left(pos)
    RightNode = MikeTree.right(pos)
    PosVal=pos.element()
    if LeftNode is None:
        return
    elif RightNode is None:
        LeftVal=LeftNode.element()
        if LeftVal>PosVal:
            tree._replace(pos, LeftVal)
            tree._replace(LeftNode,PosVal)
            max_heapify(tree,LeftNode)
    else:
        LeftVal=LeftNode.element()
        RightVal=RightNode.element()
        if RightVal>=LeftVal and RightVal>PosVal:
            tree._replace(pos,RightVal)
            tree._replace(RightNode,PosVal)
            max_heapify(tree,RightNode)
        elif LeftVal>=RightVal and LeftVal>PosVal:
            tree._replace(pos,LeftVal)
            tree._replace(LeftNode,PosVal)
            max_heapify(tree,LeftNode)
    
def build_heap(tree):
        ListPos=tree.breadthfirst_array()
        L=len(ListPos)
        if L==1 or L==0:
            return
        L2=math.floor(L/2.0)
        for pos in ListPos[L2-1::-1]:
            max_heapify(tree,pos)

def sortHeap(tree):
    build_heap(tree)
    L=MikeTree._size
    ListPos=tree.breadthfirst_array()
    L=len(ListPos)
    sortedVal=[]
    for pos in ListPos[L-1:0:-1]:
        sortedVal.append(MikeTree.root().element())
        tree._replace(MikeTree.root(), pos.element())
        MikeTree._delete(pos)
        max_heapify(MikeTree,MikeTree.root())
    return sortedVal    
    
        
