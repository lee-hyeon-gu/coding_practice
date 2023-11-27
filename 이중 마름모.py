m=int(input("큰 마름모의 한 변의 길이"))
n=int(input("작은 마름모의 한 변의 길이"))

while m<=n:
    print("불가능한 수, 다시 입력하시오")
    m=int(input("큰 마름모의 한 변의 길이"))
    n=int(input("작은 마름모의 한 변의 길이"))
    if m==n:
        print("불가능한 수")
        break

for i in range(1,n+1):
    print(' '*(m-i),end='')
    print('*'*((2*i)-1))

#여기서 그림자 추가
for i in range(n+1,m):
    
    print(' '*(m-i),end='')
    print('*'*(((n))),end='')
    print(' '*(((i-n)*2)-1),end='') 
    print('*'*(((n))))
    
for i in range(m,n,-1):
    
    print(' '*(m-i),end='')
    print('*'*(((n))),end='')
    print(' '*(((i-n)*2)-1),end='') 
    print('*'*(((n))))
#그림자 끝

for i in range(n,-1,-1):
    print(' '*(m-i),end='')
    print('*'*((2*i)-1))