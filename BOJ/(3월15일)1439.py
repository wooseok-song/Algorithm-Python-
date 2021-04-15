s=input() #input으로 숫자를 받는다.

count=0

for i in range(len(s)-1):# 마지막 까지 
    if s[i]!=s[i+1]: # 앞에 숫자가 다른경우 count를 더해준다.
        count+=1

print((count+1)//2)# count를 1을 더해 2로 나누어 준다.