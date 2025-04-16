# 테스트 케이스 수 입력
from itertools import combinations


T = int(input("테스트 케이스 수를 입력하세요: "))
# 결과 저장 및 처리
results = []
for t in range(1,T+1):
    N = int(input())

    # 홀수면 바로 Bob이 승리
    if N % 2 == 1:
        results.append("Bob")
    else:
        # 짝수일 경우 자르는 횟수를 계산
        count = 0
        while N % 2 == 0:
            N //= 2
            count += 1

        # 자르는 횟수에 따라 승자 결정
        winner = "Alice" if count % 2 == 1 else "Bob"
        results.append(winner)

# 결과 출력

    print(result)
