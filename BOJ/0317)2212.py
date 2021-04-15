import sys

n=int(input())
k=int(input())

s=list(map(int,sys.stdin.readline().split()))

s.sort()

dist=[]

if k>=n:
    print(0)
    sys.exit(0)

for i in range(1,n):
    dist.append(s[i]-s[i-1])

dist.sort(reverse=True)

for _ in range(k-1):
    dist.pop(0)

print(sum(dist))
