"""
import sys
n=int(input())

stack=[]
result=[]
array=[]
for i in range(n):
    num=int(sys.stdin.readline())
    for j in range(1,n+2):
        
        if len(stack)==0:
            stack.append(j)
            result.append('+')
            print (" ",j,result)
            continue

    
        if stack[-1]>num   :
            stack.pop()
            result.append('-')
        elif stack[-1]==num:
            temp=stack.pop()
            result.append('-')
            array.append(temp)
            print (" ",j,result)
            break    
        else:
            if j in array:
                continue
            else:
                stack.append(j)
                result.append('+')
        print (" ",j,result)

         
print (result)
print(array)   
      
"""
import sys

n=int(input())
s=[]
op=[]
count=1
temp=True
for i in range(n):
    num=int(sys.stdin.readline())
    
    while count<=num:
        s.append(count)
        op.append('+')
        count+=1
    
    if s[-1]==num:
        s.pop()
        op.append('-')
    else:
        temp=False

if temp==False:
    print('NO')
else:
    for i in op:
        print(i)