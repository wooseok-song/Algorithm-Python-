n=int(input())

array=list(map(int,input().split()))

array.sort()
target=1

for i in range(0,n):
    if target<array[i]:
        break
    target+=array[i]


print(target)
    

  
    