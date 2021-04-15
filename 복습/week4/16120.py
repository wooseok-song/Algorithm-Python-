target=input()

if target=='p':
    print("PPAP")

stack=[]
ppap=['P','P','A','P']

for t in target:
    stack.append(t)
    if stack[-4:]==ppap:
        stack.pop()
        stack.pop()
        stack.pop()

if stack==ppap or stack==['P']:
    print('PPAP')
else:
    print('NP')

