# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:30:51 2018

@author: admin
"""

val=int(input())
N=1
while True: 
   if (N*N+N)/2>val:
       pref=((N-1)*(N-1)+(N-1))/2
       X=val-pref
       Y=N+1-X
       if N%2==0:
           print(str(int(X))+'/'+str(int(Y)))
       else:
           print(str(int(Y))+'/'+str(int(X)))
       break
   elif (N*N+N)/2==val:
       if N%2==0:
           print(str(N)+'/1')
       else:
           print('1/'+str(N))           
       break
   else:
       N+=1
       continue