n,m=map(int,input().split())

result=0
val=0
for i in range(n):
    data=list(map(int,input().split()))
    if val<min(data):
        val=min(data)

print (val)