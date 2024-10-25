# 1. 입력은 10개로 정해져있음 그러므로 10 +1 돌면 됨
# 2. 각 반복에서 건물 수, 높이 받음
# 3. 결과변수 만들고
# 4. 시작, 끝 00 이니까 2, N-1 돌면서
# 5. 좌2,1, 우2,1 중 가장 높은 건물 맥스
# 6. 지금 건물이 맥스친 것보다 크면
# 7. 지금건물 - 맥스 = 결과
# 8. 리턴 결과



def count_appartment(n,height):
    result =0
    
    for i in range(2,n-2):
        max_appartment =max(height[i-1],height[i-2],height[i+1],height[i+2])
        
        if height[i] > max_appartment:
            result += height[i] - max_appartment
            
    return result



for t in range(1, 11):
    n = int(input())
    height = list(map(int, input().split()))
    result = count_appartment(n,height)
    print(f"#{t} {result}")
    
    
