def solution(s):
    min_length = len(s)  
    for c in range(1, len(s) // 2 + 1):   #단위 자르기 반까지 !
        compressed = ""
        block = s[:c]  #0부터 c까지 지금 블록 생성  "a"  
        count = 1 # 초기 카운트 1주고
    

        for i in range(c, len(s), c): # 블록단위로 점프하면서 카운트 해야함 
            current = s[i:i+c]  # 다음블록임!!! 문자열의 c번째 부터 i+c 까지 슬라이싱 "a" => "bb" 
            # print(c,i)
            if current == block: # 전 블록이랑 같으면 카운터 올리고
                count += 1
            else: # 자 틀리면 카운터 + 전 블록 넣고 카운터 초기화 카운터가 1이하면 블록만 넣기
                compressed += str(count) + block if count > 1 else block  
                # 블록에 다음 블록 넣고 카운터 초기화
                block = current 
                count =1
                
        # 남은 블럭 넣고 최소값 갱신
        compressed += str(count) + block if count > 1 else block 
        min_length = min(min_length, len(compressed))
        
        
    return min_length
                
