# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:45:33 2018

@author: admin
"""

string=input()
a_ascii=ord("a")
p=[-1 for i in range(26)]
for i in range(len(string)):
    if p[ord(string[i])-a_ascii]==-1:
        p[ord(string[i])-a_ascii]=i
for v in p:
    print(v,end=' ')