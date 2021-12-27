# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:26:07 2018

@author: admin
"""

string=input()
s=string.upper()
char_count=dict()
for c in s:
    if not c in char_count.keys():
        char_count[c]=1
    else:
        char_count[c]=char_count[c]+1
        
count_char=dict()
for key,value in char_count.items():
    if not value in count_char.keys():
        count_char[value]=[key]
    else:
        count_char[value].append(key)


if len(count_char[max(count_char.keys())])>1:
    print('?')
else:
    print(count_char[max(count_char.keys())][0])