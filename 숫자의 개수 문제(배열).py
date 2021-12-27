# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:00:34 2018

@author: admin
"""
temp=1
loop_count=0
while loop_count<3:
    ip=int(input())
    if ip>=100 and ip<1000: 
        temp*=ip
        loop_count+=1
    
for num_char in range(10):
    print(str(temp).count(str(num_char)))