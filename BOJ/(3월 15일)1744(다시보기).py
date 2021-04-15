"""
import sys

n=int(input())
arr=[]
res=0
stack=[]

for _ in range(n):
    tmp=sys.stdin.readline().strip()
    arr.append(tmp)

arr.sort(reverse=True)
for a in arr:
    k=int(a)
    stack.append(k)
    
    if k<0:
        if len(stack)!=0 and stack[-2]>0:
            res+=stack.pop()+stack.pop()
        elif len(stack)!=0 and stack[-2]<0:
            res+=stack.pop()*stack.pop()     
    elif k==0:
        if len(stack)!=0 and stack[-2]>0:
            res+=stack.pop()+stack.pop()
        elif stack[-2]<0:
            stack.append(k)
    if len(stack)==2:
        res+=stack.pop()*stack.pop()
          
print(res)
"""
import sys

n=int(input())

pn=[] #positive 방면에 대한 case

nn=[] #음수에 대한 case

en=[] #나머지에 대한 case

for i in range(n): #먼저 n 까지
    num=int(input())    #input을 분류해준다
    if num>1:
        pn.append(num)
    elif num<0:
        nn.append(num)
    else:
        en.append(num)

pn.sort(reverse=True) #이때 positive는 큰 순서대로 나열

nn.sort()       #negative는 작은 순으로 나열

res=0       

if len(pn)%2==0: #먼저 양수에 대해서 2의배수 개가 있다면 모두 곱해서 더해준다
    for i in range(0,len(pn)-1,2):
        res+=pn[i]*pn[i+1]
if len(pn)%2!=0:    #아닌경우에는 마지막 하나만 더해주고 나머지 모두 곱해서 더해준다.
    for i in range(0,len(pn)-1,2):
        res+=pn[i]*pn[i+1]
    res+=pn[-1]

if len(nn)%2==0:# 음수의 경우 2의 배수일경우 모두 곱해서 더해준다.
    for i in range(0,len(nn)-1,2):
        res+=nn[i]*nn[i+1]
if len(nn)%2!=0: # 2의 배수가 아닐경우 2의 배수만큼 곱해주고 마지막 숫자에서 0 이 없다면 단순히 더해준다.
    for i in range(0,len(nn)-1,2):
        res+=nn[i]*nn[i+1]
    if 0 not in en:
        res+=nn[-1]

res+=sum(en) #나머지 값들은 더해준다.

print(res) #결과 출력