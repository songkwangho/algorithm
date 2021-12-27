# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 13:21:54 2018

@author: admin
"""
phone={'a':1,'b':1,'c':1,'d':2,'e':2,'f':2,'g':3,'h':3,'i':3,'j':4,'k':4,'l':4,'m':5,'n':5,'o':5,'p':6,'q':6,'r':6,'s':6,'t':7,'u':7,'v':7,'w':8,'x':8,'y':8,'z':8}
in_str=input().lower()
out_num=len(in_str)
for c in in_str:  
    out_num+=phone[c]+1
print(out_num)