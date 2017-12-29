# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:50:22 2017

@author: Micha
"""

class node(object):
    def __init__(self,val=None):
        self.value=val
        self.next=None
    def setValue(self,val):
        self.value=val
    def setNext(self,nextNode):
        self.next=nextNode
    
class linkList(object):
    def __init__(self):
        self.head=None
        self.cur=None
        self.len=0
    def add(self,value):
        #add node to begin with value=value.  newNode becomes the head
        newNode=node(value)
        if self.len==0:
            newNode.next=None
            self.head=newNode
            self.cur=newNode
            self.len +=1
        else:
            newNode.next=self.head
            self.head=newNode
            self.len+=1
    def setCur(self,ind):
        if ind>self.len:
            raise Exception('error: longer than list')
        else:
            k=0
            self.cur=self.head
            while k<ind:
                self.cur=self.cur.next
                k=k+1
    def nextNode(self):
        #move to next node
        if self.cur.next==None:
            raise Exception('error end of list')
        else:
            self.cur=self.cur.next
    def insertNode(self,value,index):
        #insert node with specified value after node index
        if index>=self.len:
            raise Exception('index longer than list')
        else:
            self.len+=1
            self.setCur(index)
            tempNext=self.cur.next
            newNode=node(value)
            newNode.setNext(tempNext)
            self.cur.setNext(newNode)            
    def print(self):
        #print all values
        ind=0
        tempNode=self.head
        print(tempNode.value)
        while tempNode.next != None:
            tempNode=tempNode.next
            print(tempNode.value)
        
            
    
        