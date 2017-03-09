#!/usr/bin/python3

import sys
from math import sqrt,ceil

T = int(input())

for i in range(T):
    n = int(input())

    if n == 1:
        isprime = False
    if n == 2:
        isprime = True
    else:
        isprime = True
        for j in range(2,ceil(sqrt(n))+1):
            if n % j == 0:
                isprime = False
                break 

    if isprime:
        print("Prime:", n)
    else:
        print("Not prime:", n)
