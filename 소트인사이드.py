# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:30:46 2018

@author: admin
"""

N=input()
L=list()
for i in range(len(N)):
    L.append(int(N[i]))
    
L.sort(reverse=True)
R=str()
for j in range(len(L)):
    R+=str(L[j])
print(R)