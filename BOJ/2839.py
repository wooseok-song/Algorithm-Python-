target=int(input("N killogram"))
a=[5,3]

count=0
max=int(target/3)+1
for i in range(0,max): # i는 0,1
    
    temp=target #temp==4
    count=0 
    
    for j in a:
        if a==5:
            count+=((temp//j)-i) #count==0
            temp-=a*count      #temp==4
        else :
            count+=temp//j     #count==1
            temp %=j           #temp==1
        if count<=0:
            break
            
    if temp==0:
        break

    if i==max and temp!=0:
        count=-1   
        break
    
  
print(count)