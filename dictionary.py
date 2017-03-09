import sys

phoneBook = {}

n = int(sys.stdin.readline())

for i in range(0,n):
    entry = sys.stdin.readline().split()
    phoneBook[entry[0]] = entry[1]

query = sys.stdin.readline().strip()
while (query != ""):
    if query in phoneBook:
        print "%s=%s" % (query, phoneBook[query])
    else:
        print "Not found"
    query = sys.stdin.readline().strip()
