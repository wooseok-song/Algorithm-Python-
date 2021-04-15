import sys

n=int(input())

li=[sys.stdin.readline().strip() for _ in range(n)]
li=list(set(li))
li.sort()
li.sort(key=lambda x:len(x))


for k in li:
    print(k)