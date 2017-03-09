#!/usr/bin/python3


import sys

time = input().strip().split(":")

if time[2][2] == 'A':
   offset = 0
elif time[2][2] == 'P':
   offset = 12
else:
   print("Invalid meridiem format")
   offset = -1

if offset >= 0:
   hour = int(time[0]) % 12 + offset
   minute = time[1]
   second = time[2][:2]
   print("%.2d:%s:%s" % (hour, minute, second))

