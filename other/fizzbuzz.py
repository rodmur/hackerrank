#!/usr/bin/python3

for i in range(1,101):
    if i % 3 == 0:
        print("Fizz", end='')
    if i % 5 == 0:
        print("Buzz", end='')
    if i % 3 and i % 5:
        print(i, end='')
    print()
