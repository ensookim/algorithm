T = int(input())  # 테스트 케이스 수 입력
for case_number in range(1, T + 1):
    N = int(input())  # 각 테스트 케이스의 날 수 입력
    prices = list(map(int, input().split()))  # 매매가 입력
    max_profit = 0
    max_price = 0

    # 오른쪽에서부터 가격을 확인하여 최대 판매 가격을 찾습니다.

    for price in reversed(prices): #각 가격튜플 돌기
        if price > max_price: # 역순으로 > 전 날의 가격이 다음날 보다 높으면 살 필요가없으니 제외하고
            max_price = price
        # 현재 가격이 최대 가격보다 낮으면, 최대 이익을 계산합니다.
        max_profit += max_price - price

    # 결과 출력
    print(f"#{case_number} {max_profit}")
    
    
    
    # 입력받고
    # for로 날 수 입력받고 매매가 받고 최대값과 이익넣고
    # for 각 리스트 역순으로 돌면서 최대값보다 크면 최대값 바꾸고
    # 아니면 이윤 = 최대값 - 현제 가격