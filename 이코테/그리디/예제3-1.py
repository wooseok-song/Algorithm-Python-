n=int(input())

coin=[500,100,50,10]
cnt=0
for a in coin:
    cnt+=n//a
    n=n%a

print(cnt)