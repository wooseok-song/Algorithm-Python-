import sys

s=list(sys.stdin.readline().strip())

print(s)

stack=[]

for i in range(len(s)):
    tok=s[i]
    
    if tok=='(':
        stack.append('(')
    elif tok==')':
        