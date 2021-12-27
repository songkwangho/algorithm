# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:13:44 2018

@author: admin
"""

#num=int(input())
#count_lst=list()
#for i in range(num):
#    x,y=input().split(' ')
#    x,y=int(x),int(y)
#    if x>=0 and x<y and x<pow(2,31):
#        L=y-x
#        if L==1:
#            count_lst.append(1)
#            print(1)
#        elif L==2:
#            count_lst.append(2)
#            print(2)
#        else:
#            j=2
#            while True:
#                if L<=pow(j,2):
#                    count_lst.append(j*2-1)
#                    print(j*2-1)
#                    break
#                elif L<=(pow(j,2)+j):
#                    count_lst.append(j*2)
#                    print(j*2)
#                    break
#                else:
#                    j=+1
#for c in count_lst:
#    print(c)
import sys

num=int(sys.stdin.readline())
for i in range(num):
    x,y=map(int,input().split())
    if x>=0 and x<y and y<pow(2,31):
        L=y-x
        if L==1:
            print(1)
        elif L==2:
            print(2)
        else:
            j=2
            while True:
                if L<=pow(j,2):
                    print(j*2-1)
                    break
                elif L<=(pow(j,2)+j):
                    print(j*2)
                    break
                else:
                    j+=1
                    continue
