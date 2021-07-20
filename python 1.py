# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def multiply(a,b,bound):
    if (a*b)<=bound:
        return a*b
    else:
        return 'multiplication of {} and {} with bound {} not possible'.format(a,b,bound)

k=int(input('number of queries ='))
for i in range(k):
    a,b,bound=input().split()
    print(multiply(int(a),int(b),int(bound)))
        

