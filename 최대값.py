# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:09:26 2020

@author: admin
"""

num_list=list()
for i in range(9):
    num_list.append(int(input()))
print(max(num_list))
print(1+num_list.index(max(num_list)))