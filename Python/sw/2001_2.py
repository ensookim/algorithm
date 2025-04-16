T = int(input())  # 테스트 케이스의 개수

for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N은 그리드 크기, M은 부분 그리드 크기
    flyMap = [list(map(int, input().split())) for _ in range(N)]  # flyMap 입력 받기

    result = 0  # 최대 합을 저장할 변수

    # MxM 부분 그리드의 왼쪽 위 꼭지점 (i, j)부터 모든 가능한 위치 탐색
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            # MxM 부분 그리드 내 값을 합산
            for k in range(i, i + M):
                for p in range(j, j + M):
                    cnt += flyMap[k][p]  # 올바르게 flyMap[k][p]로 수정

            # 현재 합이 더 크면 결과 업데이트
            if result < cnt:
                result = cnt

    # 현재 테스트 케이스의 결과 출력
    print(f"#{test_case} {result}")
