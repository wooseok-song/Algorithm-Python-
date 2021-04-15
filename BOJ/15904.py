string=input() #input으로 string을 받아준다.

def find(string,f): #find함수 def 여기서 
    if f in string: #f in string을 통해서 f를 string내부에 있다면 
        return string.index(f) #return index
    return -1

fs=['U','C','P','C'] #list에 target을 넣어준다.

flag=True

for i in range(len(fs)): 
    idx=find(string,fs[i])#find함수를 이용해 찾아
    if idx!=-1:
        string=string[idx+1:] #slicing을 통해서 날려준다.
    else:
        flag=False
        break

if flag:
    print('I love UCPC')
else:
    print('I hate UCPC')