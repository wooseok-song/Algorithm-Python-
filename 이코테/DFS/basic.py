"""
from collections import deque

queue=deque()

queue.append(5)
queue.append(2)
queue.append(3)

print(queue)
queue.reverse()
print(queue)
"""
"""
INF=99999999999

graph=[
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

print(graph)
"""

"""
graph=[[]for _ in range(3)] #노드와 거리에 대한 정보.

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)
"""

