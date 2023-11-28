import random

num_list=[0,1,2,3,4,5,6,7,8,9]
answer_list=random.sample(num_list,3)

print(answer_list)

count=1 
 
for count in range(10) :
    ball=0
    strike=0
    
    a,b,c=input('숫자 세개 입력').split(',')
    q_list=[int(a),int(b),int(c)]
    
    
    
    for i in range(0,3):
        if answer_list[i]==q_list[i]:
            strike+=1
            
        elif answer_list[i]!=q_list[i]:
            ball+=1
                    
                    
    print(f'결과 {strike}S, {ball}B.')  
    
    if answer_list==q_list:
        print(f'축하합니다! {count}번만에 정답을 맞추셨습니다.')
        break
    count+=1
    
    
    
    
    

        
         
    
    
    
    
    
    
    
    

    