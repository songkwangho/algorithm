# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:13:52 2020

@author: admin
"""

N=int(input())
num_lst=[i for i in map(int, input().split())]
print('{} {}'.format(min(num_lst),max(num_lst)))