import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


N= int(input())
bamboo = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]* N for _ in range(N)]


def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]


    dp[x][y] = 1 # 지금 자리도 1로 처야됨

    #방향을 탐색해
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < N and 0 <= ny < N and bamboo[x][y] < bamboo[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)

    return dp[x][y]

max_step = 0
for i in range(N):
    for j in range(N):
        max_step = max(max_step, dfs(i,j))

print(max_step)