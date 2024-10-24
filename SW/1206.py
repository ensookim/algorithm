# 1. 입력은 10개로 정해져있음 그러므로 10 +1 돌면 됨
# 2. 각 반복에서 건물 수, 높이 받음
# 3. 결과변수 만들고
# 4. 시작, 끝 00 이니까 2, N-1 돌면서
# 5. 좌2,1, 우2,1 중 가장 높은 건물 맥스
# 6. 지금 건물이 맥스친 것보다 크면
# 7. 지금건물 - 맥스 = 결과
# 8. 리턴 결과


def apartments(N, heights):
    result = 0
    
    # 2번째 건물부터 N-3번째 건물까지 확인
    for i in range(2, N - 2):
        
        max_height = max(heights[i-2], heights[i-1], heights[i+1], heights[i+2])
        
        # 현재 건물이 좌우 2칸의 건물보다 높을 때
        if heights[i] > max_height:
            result += heights[i] - max_height
            
    return result

# 입력 : T, 각 for 에서 건물의 개수


for t in range(1, 11):
    N = int(input())  # 건물의 개수
    
    heights = list(map(int, input().split()))  # 각 건물의 높이 리스트 입력받고
    result = apartments(N, heights)
    print(f"#{t} {result}")
