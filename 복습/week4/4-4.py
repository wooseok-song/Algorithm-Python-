n,m=map(int,input().split())

x,y,direction=map(int,input().split())

togo=[[0]*m for _ in range(n)]
togo[x][y]=1

array=[]
for i in range(n):
    array.append(list(map(int,input().split())))


dx=[-1,0,1,0]
dy=[0,1,0,-1]



def turnleft():
    global direction
    if direction==3:
        direction=0
    direction+=1

count=1
turn_time=0
while True:
    turnleft()
    nx=x+dx[direction]
    ny=y+dy[direction]

    if togo[nx][ny]==0 and array[nx][ny]==0:
        x,y=nx,ny
        togo[nx][ny]=1
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1

    if turn_time==4:
        nx=x-dx[direction]
        ny=y-dy[direction]

        if array[nx][ny]==0:
            x,y=nx,ny
        else:
            break
        turn_time=0

print(count)

    

    

