#!/usr/bin/python3

import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

swaptally = 0
for i in range(n):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            swaptally += 1
    if swaptally == 0:
        break

print("Array is sorted in %d swaps." % (swaptally))
print("First Element:", a[0])
print("Last Element:", a[n-1])
