n=int(input())
plans=input().split()

x=1 
y=1
move=['L','R','U','D']

dx=[0,0,-1,1]
dy=[-1,1,0,0]


for plan in plans:
    for i in range(len(move)):
        if plan==move[i]:
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<1 or ny <1 or nx>n or ny>n:
                continue
            else:
                x+=dx[i]
                y+=dy[i]

print(x,y)
    