N = int(input())  # N 입력 받기
bamboo = [list(map(int, input().split())) for _ in range(N)]  # 대나무 높이 입력 받기
dp = [[-1] * N for _ in range(N)]  # dp 배열 초기화 (-1로 시작)

# 상하좌우 이동을 위한 dx, dy 배열
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(x, y):
    if dp[x][y] != -1:  # 이미 계산된 곳은 바로 반환
        return dp[x][y]

    dp[x][y] = 1  # 기본적으로 현재 칸은 1로 시작 (자기 자신만 포함)

    # 4방향 탐색
    for direction in range(4):
        nx, ny = x + dx[direction], y + dy[direction]

        if 0 <= nx < N and 0 <= ny < N and bamboo[x][y] < bamboo[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)  # 더 긴 경로가 있다면 갱신

    return dp[x][y]

# 모든 칸에 대해 dfs를 실행하여 가장 긴 경로를 구함
step = 0
for i in range(N):
    for j in range(N):
        step = max(step, dfs(i, j))  # 가장 긴 경로를 찾기

print(step)  # 결과 출력
