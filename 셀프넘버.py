# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:34:36 2018

@author: admin
"""

#def d(n_lst):#시간 초과 
#    idx=0
#    while idx!=len(n_lst):#인덱스 이동
#        count=0
#        prev=n_lst[idx]
#        nxt=prev
#        while nxt<=10000:            
#            temp=nxt
#            prev=nxt
#            while (temp//10)!=0:
#                nxt+=temp%10
#                temp//=10
#            if temp%10!=0:
#                nxt+=temp
#            if count!=0:
#                if prev in n_lst:
#                    n_lst.remove(prev)
#            count+=1          
#        idx+=1

def d(n_lst):
    for z in range(0,10):
        for k in range(0,10):
            for x in range(0,10):
                for y in range(0,10):
                    if (1001*z+101*k+11*x+2*y) in n_lst:
                        n_lst.remove((1001*z+101*k+11*x+2*y))

lst=[i for i in range(1,10001)]
d(lst)
for num in lst:
    print(num)


