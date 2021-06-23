import sys
import heapq
from collections import deque


input=sys.stdin.readline

n=int(input())
m=int(input())

graph=[[] for _ in range(n)]



for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    

print(graph)

pq=[]
pq.heappush(graph)

print(pq)