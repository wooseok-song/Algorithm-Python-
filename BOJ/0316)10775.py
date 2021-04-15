import sys

g=int(input())
p=int(input())

k=[]
for i in range(p):
    val=int(input())
    k.append(val)

s=[0 for _ in range (g)]
cnt=0
for a in k:
    if s[a-1]==0:
        s[a-1]=1
        cnt+=1
    else:
        t=0
        while s[a-1-t]==1 and a-1-t>0:
            t+=1
        if a-1-t==0:
            break
        s[a-t]=1
        cnt+=1

    
print(cnt)

    


