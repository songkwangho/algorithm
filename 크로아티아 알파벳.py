# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 10:52:20 2018

@author: admin
"""

import re
p=re.compile('(c=)|(c-)|(dz=)|(d-)|(lj)|(nj)|(s=)|(z=)')
in_str=input()
l=len(in_str)
c_c=0
for c_w in re.finditer(p,in_str):
    l-=len(c_w.group())
    c_c+=1
print(l+c_c)