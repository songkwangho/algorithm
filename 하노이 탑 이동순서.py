# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:52:19 2020

@author: admin
"""
def hanoi(n,from_poll,to_poll,other_poll):
    if n==1:
        print("{} {}".format(from_poll,to_poll))
        return 
    else:
        hanoi(n-1,from_poll,other_poll,to_poll)
        hanoi(1,from_poll,to_poll,other_poll)
        hanoi(n-1,other_poll,to_poll,from_poll)    
    
N=int(input())
print(2**N-1)
hanoi(N,1,3,2)