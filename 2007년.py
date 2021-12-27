# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:31:39 2018

@author: admin
"""

mon=[31,28,31,30,31,30,31,31,30,31,30,31]
day=['SUN','MON','TUE','WED','THU','FRI','SAT']

m,d=map(int,input().split(' '))
print(day[(sum(mon[:m-1])+d)%7])