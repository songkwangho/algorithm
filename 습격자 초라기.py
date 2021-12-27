# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:53:54 2021

@author: admin
"""

                
def func_1( army, W,N):#시작시 안쪽만 연결된 경우
    n_onetagon_1=[[0 for i in range(N)] for i in range(3)]
    n_onetagon_1[2][0]=0          
    n_onetagon_1[1][0]=1     
    n_onetagon_1[0][0]=1#바깥쪽 연결 불가
     
    for i in range(1,N):     
        if (i==N-1):
            n_onetagon_1[2][i]=min([n_onetagon_1[0][i-1]+1, n_onetagon_1[1][i-1]+2])
        else:
            merge_2 = 1 if army[0][i]+army[0][i-1]<=W else 2
            n_onetagon_1[2][i]=min([n_onetagon_1[0][i-1]+1,n_onetagon_1[1][i-1]+merge_2])
                
        merge_1= 1 if army[1][i]+army[1][i-1]<=W else 2        
        n_onetagon_1[1][i]=min([n_onetagon_1[0][i-1]+1,n_onetagon_1[2][i-1]+merge_1])    
        
        if (i==N-1): 
            merge_0_3= 2 if army[1][i]+army[1][i-1]<=W else 3 
            merge_0_4= 3 if army[1][i]+army[1][i-1]<=W else 4
            n_onetagon_1[0][i]=min([n_onetagon_1[0][i-1]+2, n_onetagon_1[1][i-1]+3, n_onetagon_1[2][i-1]+merge_0_3, \
                                  n_onetagon_1[1][i]+1, n_onetagon_1[2][i]+1, n_onetagon_1[0][i-2]+merge_0_4])
        else:
            merge_0_1= 1 if army[0][i]+army[1][i]<=W else 2  
            merge_0_2= 2 if army[0][i]+army[0][i-1]<=W else 3  
            merge_0_3= 2 if army[1][i]+army[1][i-1]<=W else 3 
            merge_0_4= 2 if ((army[0][i]+army[0][i-1]<=W)and(army[1][i]+army[1][i-1]<=W)) else 3 if ((army[0][i]+army[0][i-1]<=W) or (army[1][i]+army[1][i-1]<=W)) else 4
            n_onetagon_1[0][i]=min([n_onetagon_1[0][i-1]+merge_0_1, n_onetagon_1[1][i-1]+merge_0_2, n_onetagon_1[2][i-1]+merge_0_3,\
                                  n_onetagon_1[1][i]+1, n_onetagon_1[2][i]+1, n_onetagon_1[0][i-2]+merge_0_4])    
    
    Trope_count=n_onetagon_1[0][N-1]
    return Trope_count

def func_2( army, W,N):#시작시 바깥쪽만 연결된 경우
    n_onetagon_2=[[0 for i in range(N)] for i in range(3)]
    n_onetagon_2[2][0]=1         
    n_onetagon_2[1][0]=0     
    n_onetagon_2[0][0]=1#안쪽 연결 불가
    
    for i in range(1,N):   
        merge_2 = 1 if army[0][i]+army[0][i-1]<=W else 2
        n_onetagon_2[2][i]=min([n_onetagon_2[0][i-1]+1,n_onetagon_2[1][i-1]+merge_2])
        
        if (i==N-1):
            n_onetagon_2[1][i]=min([n_onetagon_2[0][i-1]+1, n_onetagon_2[2][i-1]+2])
        else:
            merge_1= 1 if army[1][i]+army[1][i-1]<=W else 2        
            n_onetagon_2[1][i]=min([n_onetagon_2[0][i-1]+1,n_onetagon_2[2][i-1]+merge_1])
           
        
        if (i==N-1): 
            merge_0_3= 2 if army[0][i]+army[0][i-1]<=W else 3 
            merge_0_4= 3 if army[0][i]+army[0][i-1]<=W else 4
            n_onetagon_2[0][i]=min([n_onetagon_2[0][i-1]+2, n_onetagon_2[2][i-1]+3, n_onetagon_2[1][i-1]+merge_0_3, \
                                  n_onetagon_2[1][i]+1, n_onetagon_2[2][i]+1, n_onetagon_2[0][i-2]+merge_0_4])
        else:
            merge_0_1= 1 if army[0][i]+army[1][i]<=W else 2  
            merge_0_2= 2 if army[0][i]+army[0][i-1]<=W else 3  
            merge_0_3= 2 if army[1][i]+army[1][i-1]<=W else 3 
            merge_0_4= 2 if ((army[0][i]+army[0][i-1]<=W)and(army[1][i]+army[1][i-1]<=W)) else 3 if ((army[0][i]+army[0][i-1]<=W) or (army[1][i]+army[1][i-1]<=W)) else 4
            n_onetagon_2[0][i]=min([n_onetagon_2[0][i-1]+merge_0_1, n_onetagon_2[1][i-1]+merge_0_2, n_onetagon_2[2][i-1]+merge_0_3,\
                                  n_onetagon_2[1][i]+1, n_onetagon_2[2][i]+1, n_onetagon_2[0][i-2]+merge_0_4])
    
    Trope_count=n_onetagon_2[0][N-1]
    return Trope_count

def func_3( army, W,N):#시작시 양쪽 다 연결된 경우
    n_onetagon_3=[[0 for i in range(N)] for i in range(3)]
    n_onetagon_3[2][0]=0         
    n_onetagon_3[1][0]=0     
    n_onetagon_3[0][0]=0#모두 연결
    
    for i in range(1,N):   
        if (i==N-1):
            n_onetagon_3[2][i]=min([n_onetagon_3[0][i-1]+1,n_onetagon_3[1][i-1]+2])
        else:
            merge_2 = 1 if army[0][i]+army[0][i-1]<=W else 2
            n_onetagon_3[2][i]=min([n_onetagon_3[0][i-1]+1,n_onetagon_3[1][i-1]+merge_2])
        
        if (i==N-1):
            n_onetagon_3[1][i]=min([n_onetagon_3[0][i-1]+1,n_onetagon_3[2][i-1]+2])
        else:
            merge_1= 1 if army[1][i]+army[1][i-1]<=W else 2        
            n_onetagon_3[1][i]=min([n_onetagon_3[0][i-1]+1,n_onetagon_3[2][i-1]+merge_1])
           
        
        if (i==N-1): 
            n_onetagon_3[0][i]=min([n_onetagon_3[0][i-1]+2, n_onetagon_3[2][i-1]+3, n_onetagon_3[1][i-1]+3, n_onetagon_3[1][i]+1, n_onetagon_3[2][i]+1, n_onetagon_3[0][i-2]+4])
        else:
            merge_0_1= 1 if army[0][i]+army[1][i]<=W else 2  
            merge_0_2= 2 if army[0][i]+army[0][i-1]<=W else 3  
            merge_0_3= 2 if army[1][i]+army[1][i-1]<=W else 3 
            merge_0_4= 2 if ((army[0][i]+army[0][i-1]<=W)and(army[1][i]+army[1][i-1]<=W)) else 3 if ((army[0][i]+army[0][i-1]<=W) or (army[1][i]+army[1][i-1]<=W)) else 4
            n_onetagon_3[0][i]=min([n_onetagon_3[0][i-1]+merge_0_1, n_onetagon_3[1][i-1]+merge_0_2, n_onetagon_3[2][i-1]+merge_0_3,\
                                  n_onetagon_3[1][i]+1, n_onetagon_3[2][i]+1, n_onetagon_3[0][i-2]+merge_0_4])
    
    Trope_count=n_onetagon_3[0][N-1]
    return Trope_count

def func_4( army, W,N):#시작시 연결이 없는 경우
    n_onetagon_4=[[0 for i in range(N)] for i in range(3)]
    
    n_onetagon_4[2][0]=min([n_onetagon_4[0][N-1]+1, n_onetagon_4[1][N-1]+2, n_onetagon_4[2][N-1]+2, n_onetagon_4[0][N-2]+3]) 
    n_onetagon_4[1][0]=min([n_onetagon_4[0][N-1]+1, n_onetagon_4[1][N-1]+2, n_onetagon_4[2][N-1]+2, n_onetagon_4[0][N-2]+3])   
    merge_0= 1 if army[0][0]+army[1][0]<=W else 2
    n_onetagon_4[0][0]=min([n_onetagon_4[2][0]+1,n_onetagon_4[1][0]+1, n_onetagon_4[0][N-1]+merge_0])#모두 연결 불가
    
    for i in range(1,N):   
        
        merge_2 = 1 if army[0][i]+army[0][i-1]<=W else 2
        n_onetagon_4[2][i]=min([n_onetagon_4[0][i-1]+1,n_onetagon_4[1][i-1]+merge_2])        
        
        merge_1= 1 if army[1][i]+army[1][i-1]<=W else 2        
        n_onetagon_4[1][i]=min([n_onetagon_4[0][i-1]+1,n_onetagon_4[2][i-1]+merge_1])
        
        merge_0_1= 1 if army[0][i]+army[1][i]<=W else 2  
        merge_0_2= 2 if army[0][i]+army[0][i-1]<=W else 3  
        merge_0_3= 2 if army[1][i]+army[1][i-1]<=W else 3 
        merge_0_4= 2 if ((army[0][i]+army[0][i-1]<=W)and(army[1][i]+army[1][i-1]<=W)) else 3 if ((army[0][i]+army[0][i-1]<=W) or (army[1][i]+army[1][i-1]<=W)) else 4
        n_onetagon_4[0][i]=min([n_onetagon_4[0][i-1]+merge_0_1, n_onetagon_4[1][i-1]+merge_0_2, n_onetagon_4[2][i-1]+merge_0_3,\
                                  n_onetagon_4[1][i]+1, n_onetagon_4[2][i]+1, n_onetagon_4[0][i-2]+merge_0_4])
    
    Trope_count=n_onetagon_4[0][N-1]
    
    return Trope_count

T=int(input())#테스트 케이스의 수
for t in range(T):
    N,W=map(int, input().strip().split())    
    # N*2 = 구역 수, W=특수 소대원 수    
    army = [[i for i in map(int, input().strip().split())] for i in range(2)]
    #army[0] = inner / army[1] = outer 
    if N==1:
        print(1 if army[0][0]+army[1][0]<=W else 2)
    else:
        if (army[0][0]+army[0][N-1]<=W) and (army[1][0]+army[1][N-1]<=W):#양쪽다 연결 가능
            
            print(min([func_1( army, W,N),func_2( army, W,N),func_3( army, W,N),func_4( army, W,N)]))
        elif (army[0][0]+army[0][N-1]<=W):#안쪽만 연결 가능
                       
            print(min([func_1(army, W,N),func_4(army, W,N)]))
        elif (army[1][0]+army[1][N-1]<=W):#바깥쪽만 연결 가능
            
            print(min([func_2(army, W,N),func_4(army, W,N)]))
        else:
            
            print(func_4(army, W,N))
    # print(search_func(dp, army, W,N))