#!/usr/bin/python3

def findrank(scores, ranks, query):
    left = 0
    right = len(scores) - 1

    while True:
        if query == scores[left]:
            return ranks[left]
        if query == scores[right]:
            return ranks[right]

        if (right - left) < 2 and scores[left] > query > scores[right]:
            return ranks[right]

        half = (right - left) // 2

        if scores[left] >= query > scores[left+half]:
            right -= half
        else:   
            left += half 
            
n = int(input())
scores = list(map(int, input().split()))
m = int(input())
alice = list(map(int, input().split()))
# your code goes here

rank = 1
ranks = []
last = scores[0]
for s in scores:
    if s != last:
        rank += 1
    ranks.append(rank)    
    last = s
    
for q in alice:
    if q > scores[0]:
        print("1")
    elif q < scores[-1]:
        print(ranks[-1]+1)
    else:
        pos = findrank(scores, ranks, q) 
        print(pos)
