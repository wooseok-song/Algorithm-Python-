x,y=list(input())

y=int(y)
x=int(ord(x))-int(ord('a'))+1
steps=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

result=0

for step in steps:
    if step[0]+x>=1 and step[1]+y>=1 and step[0]+x<=8 and step[1]+y<=8:
        result+=1
    else:
        continue

print (result)



