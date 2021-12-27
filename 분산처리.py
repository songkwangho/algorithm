# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 10:43:28 2021

@author: admin
"""
# import sys
# input = sys.stdin.readline
modulo=[[0],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
T=int(input())#테스트 케이스의 수
for t in range(T):
    a,b=map(int, input().split())#데이터의 수는 a의 b승 개 
    first_num = a%10#a의 1의 자리수
    if first_num==0:
        print(10)
    elif first_num==1 or first_num==5 or first_num==6:
        print(modulo[first_num][0])
    elif first_num == 4 or first_num==9:
        upper = b%2 #승수가 몇번 인지
        print(modulo[first_num][upper-1])
    else:        
        upper = b%4 #승수가 몇번 인지
        print(modulo[first_num][upper-1])