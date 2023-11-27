import random

num_list=[0,1,2,3,4,5,6,7,8,9]
#answer_list=random.sample(num_list,3)

count=0


answer_list=[1,2,3]
print(answer_list)

a,b,c=input('숫자 세개 입력').split(',')

q_list=[int(a),int(b),int(c)]
print(q_list)

if num_list==q_list:
    print('결과 3S, 0B.')
    print(f'축하합니다! {count}번만에 정답을 맞추셨습니다.')
    
while(num_list!=q_list):
    ball=0
    strike=0
    
    a,b,c=input('숫자 세개 입력').split(',')
    
    for i in range(0,3):
        if num_list[i]==q_list[i]:
            strike+=1
        else:
            for j in q_list:
                if j in answer_list:
                    ball+=1
        
if num_list==q_list:
    print('결과 3S, 0B.')
    print(f'축하합니다! {count}번만에 정답을 맞추셨습니다.')
                    
    print(f'결과 {strike}S, {ball}B.')
    
    
    

        
         
    
    
    
    
    
    
    
    

    