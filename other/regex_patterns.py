#!/usr/bin/python3

import sys,re

N = int(input().strip())

entry = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    entry.append((firstName,emailID))

pattern = re.compile('@gmail\.com')

for f,e in sorted(entry):
    if pattern.search(e):
        print(f) 
