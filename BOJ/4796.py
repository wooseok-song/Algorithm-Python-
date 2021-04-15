
case=0
while True:
    L,P,V=map(int,input().split())
    day=0
    case+=1
    if L==0 and P==0 and V==0 :
        break

    day+=L*(V//P)
    
    if V%P<L:
        day+=V%P
    else:
        day+=L

    print("Case %d: %d"%(case,day))