T = int(input())

# 방향: 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for testCase in range(1, T + 1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    x, y, dir = 0, 0, 0  # 각 테스트 케이스마다 초기화

    for k in range(1, N * N + 1):
        matrix[x][y] = k
        nx, ny = x + dx[dir], y + dy[dir]

        # 범위와 이동 조건 확인
        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 0:
            x, y = nx, ny
        else:
            # 범위를 벗어나거나 채워진 경우 방향 전환
            dir = (dir + 1) % 4
            x, y = x + dx[dir], y + dy[dir]

    print(f"#{testCase}")
    for row in matrix:
        print(*row, sep=" ")
