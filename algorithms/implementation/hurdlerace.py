#!/usr/bin/python3

import sys


n,k = map(int, input().split())
height = list(map(int, input().split()))

maxj = k
drinks = 0
for e in height:
    if e > maxj:
        drink = e - maxj 
        maxj += drink
        drinks += drink
    
print(drinks)
