from collections import deque
import heapq

import time

array=[6,2,8,1,3,9,4,5,10,7]
heapq.heapify(array)
array=[3,4,5,6,7,4,12,13,3]

print (array)

def heapsort(a):
    n=len(a)
    a=[0]+a

    for i in range(int(n/2),0,-1):
        heapify(a,i,n)

    for j in range(n-1,0,-1):
        a[1],a[j+1]=a[j+1],a[1]
        heapify(a,1,j)



def heapify(a,h,m):
    root=a[h]
    for j in range(2*h,m-1,2):
        if j<m and a[j]<a[j+1]:
            j+=1
        if root>=a[int(j/2)]:
            break
        else:
            a[int(j/2)]=a[j]


