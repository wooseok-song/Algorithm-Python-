import sys

n=list(map(int,sys.stdin.readline().strip()))

n.sort(reverse=True)

for a in n:
    print(a,end='')