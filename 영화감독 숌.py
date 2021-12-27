# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:48:39 2020

@author: admin
"""
def end_num_checker(n):
    b1=False
    b2=False
    while n>0:
        if n%10==6 and b1==False:
            b1 = True
            n=n//10
        elif n%10==6 and b1==True and b2 == False:
            b2 = True
            n=n//10
        elif n%10==6 and b1==True and b2 == True:
            return True
        else:
            n=n//10
            b1 = False
            b2 = False
    return False

end_number=[0 for i in range(10000)]
cand_num=665
end_num_idx=0
while True:
    cand_num+=1
    if end_num_checker(cand_num):
        end_number[end_num_idx]=cand_num
        end_num_idx+=1
        if end_num_idx>=10000:
            break

N=int(input())
print(end_number[N-1])
    
    