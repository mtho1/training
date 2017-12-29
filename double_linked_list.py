# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 08:35:23 2017

@author: Micha
"""

class DoubleLinkedList:   
    class _Node:
        def __init__(self,val=None,next=None,prev=None):
            self.val=val
            self.prev=prev
            self.next=next
    class Position:
        def __init__(self,node,container):
            self._node=node
            self.container=container
        def element(self):
            return self._node.val
    def __init__(self):
        nodeHead=self._Node(val=None)
        nodeTail=self._Node(val=None)
        nodeHead.next=nodeTail
        nodeTail.prev=nodeHead
        self._head=self.Position(nodeHead,self)  #always an empty node
        self._tail=self.Position(nodeTail,self)  #always an empty node
        self.numElements=0
    def add_front(self,value):
        #add element to front with value.   returns Position of new element
        NodeNew=self._Node(val=value,prev=self._head._node,next=self._head._node.next)
        NodeNew.next.prev=NodeNew
        self._head._node.next=NodeNew
        self.numElements+=1
        return self.Position(NodeNew,self)
    def add_back(self,value):
        #add element to back with value.   returns Position of new element
        NodeNew=self._Node(val=value,prev=self._tail._node.prev,next=self._tail._node)
        NodeNew.prev.next=NodeNew
        self._tail._node.prev=NodeNew
        self.numElements+=1
        return self.Position(NodeNew,self)
    def get_prev(self,P):
        #returns Position of prior element.  if first element returns None
        nodePrior=P._node.prev
        if nodePrior is self._head._node:
            return None
        else:
            return self.Position(nodePrior,self)
    def get_next(self,P):
        #returns Position of next element.  if last element returns None
        nodeNext=P._node.next
        if nodeNext is self._tail._node:
            return None
        else:
            return self.Position(nodeNext,self)
    def insert_before(self,P,value):
        #insert value before Position P
        newNode=self._Node(value,P._node,P._node.prev)
        P._node.prev=newNode
        self.numElements+=1
        return self.Position(newNode)
    def insert_before(self,P,value):
        #insert value after Position P
        newNode=self._Node(value,P._node.next,P._node)
        P._node.next=newNode
        self.numElements+=1
        return self.Position(newNode)   
    def get_first(self):
         #returns Position of first element
        if self.numElements==0:
            return None
        else:
            return self.Position(self._head._node.next,self)
    def get_last(self):
         #returns Position of last element
        if self.numElements==0:
            return None
        else:
            return self.Position(self._tail._node.prev,self)
            
DL=DoubleLinkedList()