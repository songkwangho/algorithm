# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 11:00:44 2021

@author: admin
"""
import sys
def next_state(p,stage):
    if p=="0":
        if stage==1:
            return 2
        elif stage == 2:
            return -1
        elif stage == 3:
            return 2
        elif stage == 4:
            return 5
        elif stage == 5:
            return 6
        elif stage == 6:
            return 6
        elif stage == 7:
            return 2
        elif stage == 8:
            return 9
        elif stage == 9:
            return 6
    else:
        if stage == 1:
            return 4
        elif stage == 2:
            return 3
        elif stage == 3:
            return 4
        elif stage == 4:
            return -1
        elif stage == 5:
            return -1
        elif stage == 6:
            return 7
        elif stage == 7:
            return 8
        elif stage == 8:
            return 8
        elif stage == 9:
            return 3
    
def state_machine(pattern,stage):
    for p in pattern:
        stage=next_state(p,stage)
        if stage == -1:
            break
   
    if stage == 1 or stage == 3 or stage == 7 or stage == 8: 
        print("YES")
    else : 
        print("NO")

T=int(input())
# input=sys.stdin.readline
for i in range(T):
    pattern = input()
    pattern_lst=list(pattern)
    state_machine(pattern,1)
    
        
