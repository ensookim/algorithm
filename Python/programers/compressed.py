def solution(s):
    min_length = len(s)  
    for c in range(1, len(s) // 2 + 1):   #단위 자르기 반까지 ! ex) 8개일때 1, 2, 3, 4 개씩 
        compressed = ""
        block = s[:c]  #0부터 1,2, 3,4 개씩 블록 생성
        count = 1      # 초기 카운트
    
    # 이제 해야할 일은 블록크기만큼 점프 , 다음 블럭과 비교, 같으면 카운터 올리고 다음블럭과 비교 , 다르면 블록을 결과에 추가하고 카운터 초기화


        for i in range(c, len(s), c): # 블록단위로 점프하면서 카운트 해야함 
            current = s[i:i+c]  # 다음블록 정의 -> 1개 다음 1개  블록크기가 2 (c)면  2(c)~ 4(c +i)까지 
            # print(c,i)
            if current == block: # 전 블록이랑 같으면
                count += 1 #카운터 올려주고 


            else: #카운터 초기화 카운터가 1이상이면  str(count)+ block, 이하면 block만 추가   
                compressed += str(count) + block if count > 1 else block  
                # 블록에 다음 블록 넣고 카운터 초기화
                block = current 
                count =1
                
        # 남은 블럭 넣고 최소값 갱신
        compressed += str(count) + block if count > 1 else block 
        min_length = min(min_length, len(compressed))
        
        
    return min_length
                
