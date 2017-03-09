#!/usr/bin/python3

n,k = map(int, input().split())
S = list(map(int, input().split()))

Q = dict(zip(S, [0] * len(S)))

while True:
    for i in S:
        for j in S:
            if i != j:
                if (i + j) % k == 0:
                    Q[i] += 1

    if sum(Q.values()) == 0:
        break

    maxkey = max(Q, key=lambda key: Q[key])
    S.remove(maxkey)
    _ = Q.pop(maxkey)
    Q = dict.fromkeys(Q,0)
    n = len(S)

print(len(S))
