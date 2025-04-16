T = int(input())  # 테스트 케이스 수

for t in range(1, T + 1):
    N, M = map(int, input().split())
    fly_map = [list(map(int, input().split())) for _ in range(N)]

    # 누적합 계산 DP
    prefix_sum = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            prefix_sum[i][j] = fly_map[i][j]
            if i > 0:
                prefix_sum[i][j] += prefix_sum[i - 1][j]
            if j > 0:
                prefix_sum[i][j] += prefix_sum[i][j - 1]
            if i > 0 and j > 0:
                prefix_sum[i][j] -= prefix_sum[i - 1][j - 1]

    # M x M 영역의 최대값 찾기
    max_flies = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # (i, j)부터 (i+M-1, j+M-1)의 합 계산
            x2, y2 = i + M - 1, j + M - 1
            current_sum = prefix_sum[x2][y2]
            if i > 0:
                current_sum -= prefix_sum[i - 1][y2]
            if j > 0:
                current_sum -= prefix_sum[x2][j - 1]
            if i > 0 and j > 0:
                current_sum += prefix_sum[i - 1][j - 1]
            max_flies = max(max_flies, current_sum)



    # 결과 출력
    print(f"#{t} {max_flies}")


