import sys

n=int(input())
"""
class stack:

    def __init__(self):
        self.top=[]

    def __len__(self):
        return len(self.top)
    
    def __str__(self):
        return str(self.top[::1])

    def push(self,item):
        self.top.append(item)

    def pop(self):

        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("stack underflow")
            exit()
    def clear(self):
        self.top=[]

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("underflow")
            exit()

    def isEmpty(self):
        return len(self.top)==0

    def size(self):
        return len(self.top) 
"""
stack=[]

def meth(command,value):
    if command=='push':
        stack.append(value)
    
    if command=='pop':
        if len(stack)==0:
            print(-1)
        else:
            popd=stack.pop()
            print(popd)

    if command=='size':
        print(len(stack))

    if command=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    if command=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])


for i in range(n):
    command=sys.stdin.readline().split()
   
    if len(command)==1:
        meth(command[0],0)
    else:
        meth(command[0],command[1])

  
