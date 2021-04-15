import sys

t=int(input())

for i in range(t):
    stack=[]
    data=sys.stdin.readline().strip()
    
    for s in data:
        stack.append(s)
        if s==')' and len(stack)>=2 and stack[-2]=='(':
            stack.pop()
            stack.pop()

    if len(stack)==0:
        print("YES")
    else:
        print("NO") 
            
            

   
