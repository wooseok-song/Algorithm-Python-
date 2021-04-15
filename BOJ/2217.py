
n=int(input())
m=[int(input()) for _ in range(n)]

m.sort(reverse=True)

for i in range(n):
    m[i]*=(i+1)


print (max(m))


