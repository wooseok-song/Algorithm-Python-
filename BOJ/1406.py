"""
import sys
st=list(sys.stdin.readline().strip())
st.append('?')
temp=[]
n=int(input())

for i in range(n):
    com=sys.stdin.readline().split()
    if com[0]=="P":
        while True:
            val=st.pop()
            temp.append(val)
            if val=='?':
                break
        st.append(com[1])
        while len(temp)!=0:
            k=temp.pop()
            st.append(k)
    elif com[0]=='L':
        idx=st.index('?')
        if idx==0:
            continue
        st[idx],st[idx-1]=st[idx-1],st[idx]
    elif com[0]=='D':
        idx=st.index('?')
        if idx==len(st)-1:
            continue
        st[idx],st[idx+1]=st[idx+1],st[idx]
    elif com[0]=='B':
        if st.index('?')==0:
            continue
        while True:
            val=st.pop()
            temp.append(val)
            if val=='?':
                break
        st.pop()
        while len(temp)!=0:
            k=temp.pop()
            st.append(k)

st.remove('?')
print("".join(st))
"""

import sys

s1=list(sys.stdin.readline().strip())
s2=[]
m=int(sys.stdin.readline())
n=len(s1)

for i in range(m):
    com=com=sys.stdin.readline().strip()
    if com[0]=="P":
        s1.append(com[2])
    elif com[0]=="L" and s1 !=[]:
        s2.append(s1.pop())
    elif com[0]=="D" and s2 !=[]:
        s1.append(s2.pop())
    elif com[0]=="B" and s1 !=[]:
        s1.pop()

print("".join(s1+list(reversed(s2))))
        