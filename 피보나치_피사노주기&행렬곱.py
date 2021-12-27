# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:50:18 2018

@author: admin
"""
#def arr_mul(arr1,arr2):
#    return [[(arr1[0][0]*arr2[0][0]+arr1[0][1]*arr2[1][0]),(arr1[0][0]*arr2[0][1]+arr1[0][1]*arr2[1][1])],[(arr1[1][0]*arr2[0][0]+arr1[1][1]*arr2[1][0]),(arr1[1][0]*arr2[0][1]+arr1[1][1]*arr2[1][1])]]
#
#def multi_arr_mul(arr, n):
#    if n!=1:
#        if n%2==0:
#            return arr_mul(multi_arr_mul(arr,int(n/2)),multi_arr_mul(arr,int(n/2))) 
#        else:
#            return arr_mul(arr_mul(multi_arr_mul(arr,int(n/2)),multi_arr_mul(arr,int(n/2))),[[1,1],[1,0]]) 
#    else:
#        return arr
#
##fn=(multi_arr_mul([[1,1],[1,0]], int(input())))[0][1]
#t=int(input())
#a=[[1,1],[1,0]]
#rt=[[1,0],[0,1]]
#
#while t>0:
#    if t%2==1:
#        rt=arr_mul(rt,a)
#    a=arr_mul(a,a)    
#    t=int(t//2)
#
#print((rt[0][1])%1000000)

#피사노 주기(피보나치 수들을 공통수로 나누었을때 나머지들에는 주기성이 존재함)를 알아야만 풀수 잇는 문제
#주기의 길이가 P 이면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M을 나눈 나머지와 같습니다.
#M = 10의 k승 일 때, k > 2 라면, 주기는 항상 15 × 10의 k-1승 입니다. 이 사실을 모른다고 해도, 주기를 구하는 코드를 이용해서 문제를 풀 수 있습니다.

def fibonacci_pisano(n):
    fibo = [0, 1]
    mod = 1000000
    p = int(mod/10*15)
    i = 2
    while i < p:
        fibo.append(fibo[i-1] + fibo[i-2])
        fibo[i] %= mod
        i += 1
 
    return fibo[n%p]
 
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_pisano(n))