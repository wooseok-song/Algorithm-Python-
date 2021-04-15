p=input()
row=int(p[1])
col=int(ord(p[0]))-int(ord('a'))+1

steps=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
count=0


for step in steps:
    nx=col+step[0]
    ny=row+step[1]
    if nx<1 or ny<1 or nx>8 or ny>8:
       continue
    else:
        count+=1

print(count)

