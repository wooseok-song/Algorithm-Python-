
n=int(input())

array=[[int(x) for x in input().split()]for y in range (n)]

array.sort(key=lambda x:x[0])
array.sort(key=lambda x:x[1])
count=0
start=finish=0
for j in range(0,n):
    if finish<=array[j][0]:
        start=array[j][0]
        finish=array[j][1]
        count+=1

print (count)

#main point는 끝나는 시간도 sorting 해줌으로써 겹치는 2,2도 포함시키도록 한다.