#!/usr/bin/python3

import sys
def sumcol(A,col,n):
    sum = 0
    for i in range(n):
        sum += A[i][col]
        
    return sum    
q = int(input())
for _ in range(q):
    n = int(input())
    M = []
    for _ in range(n):
        M_t = list(map(int, input().split()))
        M.append(M_t)
        
    typesum = []
    contsum = []
    for i in range(n):
        typesum.append(sum(M[i]))
        contsum.append(sumcol(M,i,n))

    if sorted(typesum) == sorted(contsum):
        print("Possible")
    else:
        print("Impossible")
