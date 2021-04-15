n,m=map(int,input().split())
array=list(map(int,input().split()))

q=n//m
temp=[] #the array for the how many thing in the group
value=[]

for a in range(m):
    temp.append(q)
    value.append(0)
    if a==0:
        temp[0]+=n%m
    

print(temp)

Max=0
total=0
for k in range()
    for i in range(m):
        for j in range(total,total+temp[i]):
            value[i]+=array[j]   
            if Max<value[i]:
                Max=value[i]
        total+=temp[i]

print (value)

#포기.