# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 17:35:15 2018

@author: admin
"""

room_num=int(input())
count=1
if room_num>=1 and room_num<=1000000000:
    while True:
        if room_num<=((3*count*count)-(3*count)+1):
            print(count)
            break
        else:
            count+=1
    
        