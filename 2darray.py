#!/usr/bin/python3

import sys
hightotal = -70

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

for i in range(1,5):
    for j in range(1,5):
        topsum = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
        bottomsum = arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
        total = topsum + bottomsum + arr[i][j]
        if (total > hightotal):
            hightotal = total
print(hightotal)
