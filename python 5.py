# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 10:57:29 2021

@author: KAPIL
"""
import numpy as np


def vec(X,B,C):
    A = [[0 for j in range(2)] for i in range(1)]
    D = np.dot(B,C) 
    #print(D)
    A[0][0]=(X-D[1][0])/(D[0][0]-D[1][0])
    A[0][1]=1-A[0][0]
    return A

n=int(input('Number of test ='))

for i in range(n):
    X=int(input())
    #print(X)
    entries = list(map(int, input().split()))
    B= np.array(entries).reshape(2,2)
    #print(B)
    ent = list(map(int, input().split()))
    C= np.array(ent).reshape(2,1)
    #print(C)
    print(vec(X,B,C))