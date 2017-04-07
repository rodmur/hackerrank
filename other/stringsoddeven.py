import sys

T = int(sys.stdin.readline())

for i in range(0,T):
   S = sys.stdin.readline().strip('\n')
   evens = "" 
   odds = ""
   for j in range(0,len(S)):
       if (j % 2):
           odds += S[j]
       else:
           evens += S[j]
   print "%s %s" % (evens, odds)

