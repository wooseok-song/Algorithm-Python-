import sys
n,m=map(int,sys.stdin.readline().split())

a=[sys.stdin.readline().strip() for _ in range(n)]

b=[sys.stdin.readline().strip() for _ in range(m)]

a=set(a)
b=set(b)

res=a&b

res=list(res)
res.sort()

print(len(res))
for i in range(len(res)):
    print(res[i])