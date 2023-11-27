import random

rand_int = random.randint(1,100) #1~100까지의 임의의 int를 생성합니다.

print(rand_int)



num=int(input("1부터 100까지의 숫자를 맞춰보세요!"))

print('-------------------------------')
count =0
while(num!=rand_int):
    
    if num< rand_int:
        num=int(input("Up! 더 큰 숫자를 입력하세요."))
        count+=1
        print('-------------------------------')
        
    elif num> rand_int:
        num=int(input("Down! 더 작은 숫자를 입력하세요."))
        count+=1
        print('-------------------------------')
        
    elif num==rand_int:
        break
    

    if num<=0:
        break

#  while 안에 있으면 elif 까지 안가고 바로 break 하기때문에 밖에둔다
count+=1
print(f'정답입니다! {num}를 {count}번 만에 맞췄습니다')