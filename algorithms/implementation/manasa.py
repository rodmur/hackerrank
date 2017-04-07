#!/usr/bin/python3
T = int(input())
answers = []
for _ in range(T):
    n = int(input())
    a = int(input())
    b = int(input())
    for k in range(n):
        answers.append(k*a + (n-1-k)*b)
    for i in sorted(answers):
        print(i,end=" ")
    print()
    answers = []
