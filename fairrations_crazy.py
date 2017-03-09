#!/usr/bin/python3

import sys

N = int(input())
B = list(map(int, input().split()))

sum = 0
carry = False
for x in B:
   
    carry = (carry + x) & 1
    sum += carry * 2

if carry:
    print("NO")
else:
    print (sum)
