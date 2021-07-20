# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 16:07:33 2021

@author: KAPIL
"""
def even(s,n):
    while n>0:
        l=[]
        if s%2==0:
            l.append(s)
            for i in range(n-1):
                s=s+2
                l.append(s)
            break 
        else:
            s=s+1
    
    return ' '.join(map(str, l))
        

s,n=input().split()
print(even(int(s),int(n)))