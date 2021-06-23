import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())

s=[list(map(int,input().strip())) for _ in range(n)]

visited=[[0]*m for _ in range(n)]


ds=[(1,0),(0,1),(-1,0),(0,-1)]

def bfs(start):
    queue=deque()
    queue.append(start)
    while queue:
        x,y=queue.popleft()
        if visited[x][y]==0:
            visited[x][y]=1
            for i in range(4):
                nx=x+ds[i][0]
                ny=y+ds[i][1]
                if 0<=nx<n and 0<=ny<m and s[nx][ny]==1:
                    queue.append((nx,ny))
                    s[nx][ny]=s[x][y]+1


res=bfs((0,0))
print(s[n-1][m-1])
