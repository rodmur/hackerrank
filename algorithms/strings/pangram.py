#!/usr/bin/python3

import string

d = dict.fromkeys(string.ascii_uppercase,False)

S = input().strip()

for c in S:
    if c.isalpha():
        c = c.upper()
        d[c] = True
    
print(d)
if sum(d.values()) == 26:   
    print("pangram")
else:
    print("not pangram")
