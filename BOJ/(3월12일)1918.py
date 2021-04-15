a=input() #input을 이용해 문자열을 입력 받는다.

stack=[]# stack 선언
res='' #문자열 선언

for x in a:
    if x.isalpha(): #isalPha를 이용해 이것이 피연산자인지 알수있게 한다.
        res+=x #피연산자인 경우에 문자열에 추가해준다.

    else:
        if x=='(': #스택내 우선순위가 가장 낮은 것 부터 시작
            stack.append(x)# append 해준다
        elif x=='*'or x=='/': # 그 다음 우선순위를 
            while stack and(stack[-1]=='*'or stack[-1]=='/'): # stack에 값이 있고 마지막 이 * , /인 case 에대해서 pop해준뒤 모두 출력해준다.
                res+=stack.pop()
            stack.append(x)# +, - 같은 것들은 모두 출력된다.

        elif x=='+'or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)

        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()

while stack:
    res+=stack.pop()
print(res)