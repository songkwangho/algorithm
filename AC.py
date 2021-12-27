# -*- coding: utf-8 -*-
"""
Created on Mon May 28 10:16:05 2018

@author: admin
"""
import sys
T=int(input())

for i in range(T):
    try:
        test_case_func=list(input())
        test_case_arr_len=int(input())
        
        if test_case_arr_len!=0:
            test_case_arr=[int(i) for i in input().strip('[]').split(',')]
        else:
            input()
            test_case_arr=[]
        direction=True
        err=False    
        for num_tcase in test_case_func:
            if num_tcase=='D':
                if direction:
                    test_case_arr.pop(0)
                else:
                    test_case_arr.pop()
            elif num_tcase=='R':            
                direction=not direction
        
        if direction:            
            print("{}".format(str(test_case_arr).replace(' ','')))            
        else:
            print("{}".format(str(test_case_arr[::-1]).replace(' ','')))
    except:
         sys.stdout.write('error\n')