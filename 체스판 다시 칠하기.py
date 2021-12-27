# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:43:47 2020

@author: admin
"""
def numberone_counter(val):
    count=0
    while val!=0:
        val=val&(val-1)
        count+=1
    return count

black_board=['0b01010101','0b10101010','0b01010101','0b10101010','0b01010101','0b10101010','0b01010101','0b10101010']
white_board=['0b10101010','0b01010101','0b10101010','0b01010101','0b10101010','0b01010101','0b10101010','0b01010101']

N,M=map(int, input().split())
input_table=list()

for i in range(N):
    input_str=input()
    input_table.append(['0' if c=='B' else '1' for c in input_str])
min_value=3000
for i in range(7,N):#7 이후의 y점
    for j in range(7,M):#7 이후의 x점
        diff1_sum=0
        diff2_sum=0
        for k1,k2 in zip(range(7,-1,-1),range(0,8)):#8X8 한판
            diff1=numberone_counter(int(black_board[k2],base=2)^int('0b{}'.format(''.join(input_table[i-k1][j-7:j+1])),base=2))
            diff2=numberone_counter(int(white_board[k2],base=2)^int('0b{}'.format(''.join(input_table[i-k1][j-7:j+1])),base=2))
            diff1_sum+=diff1
            diff2_sum+=diff2
        cand=diff1_sum if diff1_sum<diff2_sum else diff2_sum
        min_value= min_value if min_value<cand else cand
print(min_value)
