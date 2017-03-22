#!/usr/bin/python3

def findrank(scores, ranks, query):
    sl = len(scores)
    if sl > 1: 
        half = sl // 2
        if query > scores[half][1]:
            pos = findrank(scores[:half], ranks, query)
        else:
            pos = findrank(scores[half:], ranks, query)
    else:
        result = scores[0][1]
        if q >= result:
            pos = ranks[scores[0][0]]-1 
        else:
            pos = ranks[scores[0][0]]

             
    return pos        
        
        

n = int(input())
scores = list(enumerate(map(int, input().split())))
m = int(input())
alice = list(map(int, input().split()))
# your code goes here

rank = 1
ranks = []
last = scores[0]
for _,s in scores:
    if s != last:
        rank += 1
    ranks.append(rank)    
    last = s
    
for q in alice:
    if q > scores[0][1]:
        print("1")
    elif q < scores[-1][1]:
        print(ranks[-1])
    else:
        positions = []
        pos = findrank(scores, ranks, q) 
        positions.append(pos)

for i in positions:
    print(i)
