#!/usr/bin/python3

import re, string

q = int(input())


for _ in range(q):
    a = input().strip()
    b = input().strip()

    pos = 0
    ok = True
    for k in range(len(b)):
        if k < len(b) - 1:
            patc = re.compile(r'%s\w*[%s%s]' % (b[k],b[k+1].lower(),b[k+1]))
            patl = re.compile(r'%s\w*%s' % (b[k].lower(),b[k+1]))
        else:
            patc = re.compile(b[k])
            patl = re.compile(b[k].lower())

        m = patc.search(a,pos)
        if m is None:
            m = patl.search(a,pos)
            if m is None:
                ok = False
                break
        pos = m.start()
        if a[pos].islower():
            a = a[:pos] + b[k] + a[pos+1:]
        pos = m.end()

    a = a.translate({ord(c): None for c in string.ascii_lowercase})
    print("a:", a)
    print("b:", b)
    print("ok:", ok)
    if (b == a) and ok:
        print("YES")
    else:
        print("NO")
