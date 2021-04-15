import sys

n,l=map(int,input().split())

a=list(map(int,sys.stdin.readline().strip().split()))

a.sort()
start=a[0]
end=a[0]+l
cnt=1

for i in range(n):
    if start<=a[i]<end:
        continue
    else:
        start=a[i]
        end=a[i]+l
        cnt+=1

print(cnt)