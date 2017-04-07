#!/usr/bin/python3

import sys
from math import log

high = 40
t = int(input())
table = [0]
blah = 0
for n in range(high):
    blah += 3*2**n 
    table.append(blah)
    
for i in range(high):
    if table[i] < t <= table[i+1]:
        break
        
foo = table[i+1] - t + 1

print(foo)
