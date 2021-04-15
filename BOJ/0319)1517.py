import sys

n=int(input())
t=list(map(int,sys.stdin.readline().split()))


"""
def bubbleSort(k):
    h=len(k)
    cnt=0
    for i in range(h):
        max=k[i]
        for j in range(i,h):
            if max > k[j]:
                k[j],k[i]=k[i],k[j]
                cnt+=1

    return k,cnt
"""
global swap

def merge(left,right):  #먼저 merge해주는 부분에 대한 코드이다.
    res=[] 
    cnt=0            #결과를 담는 list
    global swap
    while len(left)>0 or len(right)>0: #먼저 입력받은 list의 길이가 모두 0보다 크다면 합병을 진행한다.
            if len(left)>0 and len(right)>0:#두개 list에 모두 값이 담겨잇는경우 
                if left[0]<right[0]: #right list의 값이 더 작은경우 결과에 append해준다.
                    res.append(left[0])
                    left=left[1:]
                    cnt+=1
                else:
                    res.append(right[0])#다른 경우에는 right를 추가해주고 slicing을 이용해 배열 바꿔줌
                    right=right[1:]
                    
                    global swap+=cnt
            elif len(left)>0: #아래는 둘중 하나의 list에 값이 남아있는 경우에 대한것  나머지는 단순히 append해준다.
                res.append(left[0])
                left=left[1:]
            elif len(right)>0:
                    res.append(right[0])
                    right=right[1:]
    return res
    


def mergeSort(a): #먼저 반으로 나누어 주는 함수이다
    if len(a)<=1:
        return a
  
    m=len(a)//2#먼저 list의 길이를 반으로 나누어 준다
    left=a[:m] #slicing을 이용해 반으로 나눠준다
    right=a[m:]
    
    left=mergeSort(left) #각각 recursive하게 돌려준다
    right=mergeSort(right)
    return merge(left,right)#마지막에 merge함수 호출한다.


mergeSort(t)

print(swap)