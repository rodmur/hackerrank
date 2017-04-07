#!/usr/bin/python3
s = list(input().strip())

i = 0
n = len(s)
while s != "":
    change = False
    i = 0
    while i < n:
        if i < n-1 and s[i] == s[i+1]:
            _ = s.pop(i+1)
            _ = s.pop(i)
            change = True

        n = len(s)
        i += 1

    if not change:
        break
            
print("Empty String") if len(s) == 0 else print("".join(s))

