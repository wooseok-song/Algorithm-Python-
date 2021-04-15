"""
import sys

n=int(input())
li=list(sys.stdin.readline().strip().split())
res=''

for i in range(n):
    val=li[i]
    right=li[i:]
    stack=[]
    for a in right:
        if val<a:
            res+=a
            res+=' '
            while stack:
                stack.pop()
            break
        elif val>=a:
            stack.append(a)
    if stack :
        res+='-1 '

print(res)
        
"""

import sys

n=int(input())
li=list(sys.stdin.readline().strip().split())
stack=[]
result=[-1 for _ in range(n)]
i=1
while stack and i<n:
    while stack and li[stack[-1]]<li[i]:
       result[stack[-1]]=input[i]
       stack.pop() 
    

 
print(res)
        