#!/usr/bin/python3

import sys

s = input().strip()
t = input().strip()
k = int(input())

goldT = t

def chopitdown(s,t,k):
    global goldT

    if k == 0:
        return

    if len(s) > len(t):
        s = s[:-1]
    elif len(s) < len(t):
        s = s + t[len(s)]
    else:
        if len(goldT) - len(s) > k:
            s = s[:-1]
            t = t[:-1]
        else:
            s = s + goldT[len(s)]
    chopitdown(s,t,k-1)
        

if abs(len(s) - len(t)) > k:
    print("No")
    sys.exit(0)

chopitdown(s,t,k)

print("end s: ", s)

if s == t:
    print("Yes")
else:
    print("No")
