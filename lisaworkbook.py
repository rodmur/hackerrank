#!/usr/bin/python3

# n = chapters, k = problems per page
n,k = map(int,input().split())
# number of problems per a particular chapter
t = list(map(int,input().split()))

special = 0
page = 1
for c in t:
    p = list(range(1,c+1))
    pages = [p[i:i+k] for i in range(0,c,k)]
    
    for z in pages:
        if page in z:
            special += 1
        page += 1
            
print(special)
