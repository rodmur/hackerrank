#!/usr/bin/python3

s = input().strip()
n = int(input())

weights = set() 
add = 0
for i in range(len(s)):
    w = ord(s[i]) - ord('a') + 1
    weights.add(w)
    if i > 0 and s[i] == s[i-1]:
        add += w
        weights.add(w + add)
    else:
        add = 0

for _ in range(n):
    x = int(input())
    if x in weights:
        print("Yes")
    else:
        print("No")
    
