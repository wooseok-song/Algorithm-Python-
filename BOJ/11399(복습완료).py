#people=int(input("How many people ? \n"))
#print("Insert time! ")

people=int(input())
array=list(map(int,input().split()))

array.sort()
min=0
for i in range(0,people):
    min+=(people-i)*array[i]


print(min)