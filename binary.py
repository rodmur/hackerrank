#!/usr/bin/python3

import sys

n = int(input().strip())
expn = 0
count = 0
maxcount = 0

while (n >= 1<<expn):
    if (n & 1<<expn):
        count += 1
    else:
        count = 0
    expn += 1
    if count > maxcount:
        maxcount = count
print(maxcount)
