t=int(input())
score=[]

for i in range(t):
    case=int(input())
    score=[list(map(int,input().split()))for _ in range(case)] #2차원 배열 만들기
    score.sort( key=lambda x:x[0])
    min=score[0][1]
    count=1
    for s in score:
        if s[1]<min:
            min=s[1]
            count+=1
    
    print(count)