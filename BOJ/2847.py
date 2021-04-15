n=int(input())
s=[]
"""
for i in range(n):
    s.append(int(input()))
"""
s=[int(input()) for _ in range (n)]

s.reverse()
before=s[0]

cnt=0
for i in range(1,n):
    while s[i]>=before:
        s[i]=s[i]-1
        cnt+=1
    
    before=s[i]
print(cnt)

"""
for i in range(n-1,0,-1):#역으로 갈떄는 range를 만들어 준다 이때 마지막 부분은 step에 관한것
    if s[i]<=s[i-1]:
        result+=(s[i-1]-s[i]+1)
        s[i-1]=s[i]-1

"""