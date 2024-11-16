# 입력

N = int(input())
bamboo = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*N for _ in range(N)]
# 방문 안한 곳은 -1로 되어있어

# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

step=0
#이제 dp를 채워야함

# 깊이우선 탐색으로 끝까지 가서 최대값을 저장하는걸로

def dfs(x,y):
    if dp[x][y] != -1 :
        return dp[x][y]

    dp[x][y] = 1


    for direction in range(4):
        # 4 방향 탐색해서 함
        nx , ny = x+dx[direction], y+dy[direction]

        if 0<= nx < N and 0<=ny< N and bamboo[x][y] < bamboo[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx,ny)+1)
            # 범위 내에 있고, 다음 표의 대나무가 더 크다면

    return dp[x][y]

for i in range(N):
    for j in range(N):
        step = max(step, dfs(i,j))

print(step)














