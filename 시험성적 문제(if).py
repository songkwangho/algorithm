# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:54:25 2018

@author: admin
"""
val=int(input())
if val>= 0 and val<=200:
    if val<60:
        print('F')
    elif val<70:
        print('D')
    elif val<80:
        print('C')
    elif val<90:
        print('B')
    else:
        print('A')