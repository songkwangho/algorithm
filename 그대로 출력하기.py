# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 10:46:44 2018

@author: admin
"""

import sys
data=sys.stdin.readlines()
for i in range(len(data)):
    data[i]=data[i].replace('\n','')
    print(data[i])