a=input()

if a=='P' or a=='PPAP':
    print('PPAP')

else:
    stack=[]
    ppap=['P','P','A','P']
    for i in a:
        stack.append(i)
        if stack[-4:]==ppap:
            stack.pop()
            stack.pop()
            stack.pop()
    if stack==ppap or stack==['P']:
        print('PPAP')
    else:
        print('NP')
