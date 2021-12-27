# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:59:55 2020

@author: admin
"""
import math
A,B,V=map(int,input().split())
date=math.ceil((V-A)/(A-B))+1
print(date)