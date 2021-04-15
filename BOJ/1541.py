s=input().split('-')
result=[]
for i in range(len(s)): #이러한 방식을 되도록이면 피하는게 좋다.python 에서는
    cnt=s[i].count('+')
    temp=0
    if cnt!=0:
        t=s[i].split('+')
        for val in t:
            temp+=int(val)
    else:
        temp=int(s[i] )

    if i==0:
        result+=temp
    else :
        result-=temp
print (result)


"""
for i in s:
    cnt=0
    k=i.split('+')
    for j in k:
        cnt+=int(j)
    result.append(cnt)
n=num[0]
for i in range(1,len(num)):
    n-=num[i]
print (n)
"""