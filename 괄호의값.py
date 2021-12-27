# -*- coding: utf-8 -*-
"""
Created on Tue May  1 10:26:03 2018

@author: admin
"""
def top(lst):
    return lst[len(lst)-1]
import sys
class end(BaseException): pass
#sys.stdin.readline()
#lst=sys.stdin.readline()
lst=input()
stk=list()
try:
    for s in lst:   
        if s=='(':
            stk.append('(')
            
        elif s=='[':
            stk.append('[')
            
        elif s==')':
            add=0
            if len(stk)>0:
                tmp=stk.pop()
            else:
                raise end
            if tmp=='(':
                stk.append(2)
            else:
                while tmp != '(':
                    if tmp !='[':
                        add+=tmp
                    else:
                        raise end
                    if len(stk)>0:
                        tmp=stk.pop()
                    else:
                        raise end
                stk.append(add*2)
            
        elif s==']':
            add=0
            if len(stk)>0:
                tmp=stk.pop()
            else:
                raise end
            if tmp=='[':
                stk.append(3)
            else:
                while tmp != '[':
                    if tmp != '(':
                        add+=tmp
                    else:
                        raise end
                    if len(stk)>0:
                        tmp=stk.pop()
                    else:
                        raise end
                stk.append(add*3)
            
    if len(stk)==1:
        print(stk.pop())
    else:
        tmp=0
        while len(stk)!=0:
            k=stk.pop()
            if k =='(' or k =='[':
                raise end
            else:
                tmp+=k
        print(tmp)
except end:
    print(0)
    pass