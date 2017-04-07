#!/usr/bin/python3

import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase

n = int(input())
s = input().strip()
k = int(input()) % 26

rotup = upper[k:] + upper[:k]
rotlow = lower[k:] + lower[:k]

for i in range(n):
    if s[i].isupper():
        print(rotup[ord(s[i])-ord('A')],end='')
    elif s[i].islower():
        print(rotlow[ord(s[i])-ord('a')],end='')
    else:
        print(s[i],end='')
        
print()
