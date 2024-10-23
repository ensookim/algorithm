T = int(input())  # 테스트 케이스 수 입력



for t in range(1, T + 1):
    N = int(input())  # 각 테스트 케이스의 날 수 입력
    prices = list(map(int, input().split()))  #가격 입력
    result = 0  # 이윤
    maxPrice = 0  
    
    
    for val in prices[::-1]:
        if val >= maxPrice:
            maxPrice = val
        
        else:

            result += maxPrice -val
    

    # 결과 출력
    print(f"#{t} {result}")
    
    
    
    # 입력받고
    # for로 날 수 입력받고 매매가 받고 최대값과 이익넣고
    # for 각 리스트 역순으로 돌면서 최대값보다 크면 최대값 바꾸고
    # 아니면 이윤 = 최대값 - 현제 가격