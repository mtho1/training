# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 22:49:40 2017

@author: Micha
"""

def mikeyield():
    k=1
    yield k
    k=2
    yield k
    

class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n
        print('f')
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
    
    