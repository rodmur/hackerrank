#!/usr/bin/python3

import sys

N = int(input())
B = list(map(int, input().split()))

if sum(B) & 1:
    print("NO")
    sys.exit(0)

loafs = 0
while True:
    alleven = True
    for x in B:
        if x & 1:
            alleven = False
            break
    if alleven:
        break
        
    for i in range(N):
        B[i] += 1
        loafs += 1
        if 0 < i < len(B) - 1:
            if B[i-1] & 1:
                B[i-1] += 1
            elif B[i+1] & 1:
                B[i+1] += 1
        else: 
            if i == 0:
                B[1] += 1
            else:
                B[i-1] += 1
        loafs += 1        
print(B)            
print(loafs)
