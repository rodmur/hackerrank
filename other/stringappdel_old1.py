#!/usr/bin/python3

import sys

s = input().strip()
t = input().strip()
k = int(input())


if abs(len(s) - len(t)) > k:
    print("No")
    sys.exit(0)

for i in range(k):
    if s == "" and k - i < len(t):
        s == ""
    elif s == "" and k - i >= len(t):
        s = t[0]
        print("null stat s: ", s)
    elif s == t

print("end s: ", s)

if s == t:
    print("Yes")
else:
    print("No")
 
#    elif len(s) > len(t):
#        s = s[:-1]
#        print("gt s: ", s)
#    elif len(s) < len(t):
#        s = s + t[len(s)]
#        print("lt s: ", s)
#    elif len(s) == len(t[:len(s)]) and s != t[:len(s)]:
#        s = s[:-1]
#        print("eq1 s: ", s)
#    elif len(s) == len(t[:len(s)]) and s == t[:len(s)] and len(s) + len(t) > k:
#        s = s[:-1]
#        print("eq2 s: ", s)
