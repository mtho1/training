# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:50:22 2017

@author: Micha
"""

#a better version with encapsulation of node


    
class linkList2(object):
    class _Node(object):
        def __init__(self,val=None):
            self.value=val
            self.next=None
        def setValue(self,val):
            self.value=val
        def setNext(self,nextNode):
            self.next=nextNode
    class Position(object):  #encapsulates the node
        def __init__(self,container,node):
            self._node=node
            self._container=container
        def element(self):
            """Return the element stored at this Position."""
            return self._node.value
        def has_next(self):
            if self._node.next==None:
                return False
            else:
                return True
            
    def __init__(self):
        self.head=None  #a position (once implemented)
        self.cur=None   # a position (once implemented)
        self.len=0
    def add(self,value):
        #add node to begin with value=value.  newNode becomes the head
        newNode=self._Node(value)
        if self.len==0:
            newNode.next=None
            self.head=self.Position(self,newNode)
            self.cur=self.head
            self.len +=1
        else:
            newNode.setNext(self.head._node)
            self.head=self.Position(self,newNode)
            self.len+=1
        return self.Position(self,newNode)
    def setCur(self,ind):
        if ind>self.len:
            raise Exception('error: longer than list')
        else:
            k=0
            self.cur=self.head
            while k<ind:
                self.cur=self.Position(self,self.cur._node.next)
                k=k+1
            return self.cur
    def nextNode(self):
        #move to next node
        if self.cur._node.next==None:
            raise Exception('error end of list')
        else:
            self.cur=self.Position(self,self.cur._node.next)
            return self.cur
    def insertNode(self,value,index):
        #insert node with specified value after node index
        if index>=self.len:
            raise Exception('index longer than list')
        else:
            self.len+=1
            self.setCur(index)   #this can be slow
            tempNext=self.cur._node.next # a node
            newNode=self._Node(value)   #a node
            newNode.setNext(tempNext) 
            self.cur._node.setNext(newNode)  #update current
            return self.Position(self,newNode)            #position of current node
    def print(self):
        #print all values
        ind=0
        tempPos=self.setCur(0)
        print(tempPos._node.value)
        while tempPos._node.next != None:
            tempPos=self.nextNode()
            print(tempPos.element())
        
            
    
        