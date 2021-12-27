# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:36:12 2020

@author: admin
"""

def make_stars(n,x,y,s):
    if n==3:
        s[x][y]='*'        
        s[x+1][y]='*'        
        s[x+2][y]='*'
        
        s[x][y+1]='*'        
        s[x+2][y+1]='*'
        
        s[x][y+2]='*'        
        s[x+1][y+2]='*'        
        s[x+2][y+2]='*'
        return
    else:
        make_stars(n//3,    x,  y,  s)
        make_stars(n//3,    x+n//3, y,  s)
        make_stars(n//3,    x+(n//3)*2, y,  s)
        
        make_stars(n//3,    x,  y+n//3,s)
        make_stars(n//3,    x+(n//3)*2, y+n//3,s)
        
        make_stars(n//3,    x,  y+(n//3)*2,s)
        make_stars(n//3,    x+n//3, y+(n//3)*2,s)
        make_stars(n//3,    x+(n//3)*2, y+(n//3)*2,s)
    return  

N=int(input())
stars=[[' ' for i in range(N)] for i in range(N)]

make_stars(N,0,0,stars)
for star in stars:
    print(''.join(star))