# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 16:28:48 2021

@author: KAPIL
"""
def appended(l,v):
    if l==[]:
        l.append(v)
    else:
        while l[-1]>v:
            l.pop()
        l.append(v)
def popped():
    l.pop()
    
def size():
    return print(len(l))

l=[]

n = int(input('Number of queries='))
for i in range(n):
    inp=input().split()
    input1=inp[0]
    if input1 == "append":
        val = int(inp[1])
        appended(l,val)
    elif input1 == "pop":
        popped()
    elif input1 == "size":
        size()
    else:
        raise ValueError("invalid operation")