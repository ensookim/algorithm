T = int(input())  # 테스트 케이스 수 입력
for t in range(1, T + 1):  # 테스트 케이스만큼 반복
    P, Q, R, S, W = map(int, input().split())  # P, Q, R, S, W 입력 받기
    # A사 요금 계산
    A = P * W
    
    # B사 요금 계산
    if W > R:
        B = Q + (W - R) * S  # 기본 요금 Q + 초과량에 따른 요금
    else:
        B = Q  # 기본 요금만
    
    # 더 저렴한 요금 선택
    company = min(A, B)
    
    # 출력
    print(f"#{t} {company}")
