n=int(input())

string=[input() for _ in range (n)]
string.sort(reverse=True, key=len)
length=[]

for i in range(n):
    length.append(len(string[i]))
length.append(0)

b=[9,8,7,6,5,4,3,2,1,0]
count=0
for i in range(n):
    temp=string[i]
    for j in range(0,length[i]-length[i+1]):
        Char=temp[j]
        temp[j]=a[count]
        count+=1
   

print(string)




