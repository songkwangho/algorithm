# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 11:46:39 2018

@author: admin
"""
import math

room_num=input()
lst=[0 for i in range(10)]

for n in room_num:
    lst[int(n)]+=1
    
lst[9]=math.ceil((lst[9]+lst[6])/2)
lst[6]=0
print(max(lst))