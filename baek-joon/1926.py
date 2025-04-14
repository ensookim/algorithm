# 1이 연속된 것의 개수와, 최대값 구하기 BFS

# 1. 아이디어 : 2중 FOR를 돌면서 -> 값이 1 AND 방문 X => BFS
# BFS 돌면서 그림 개수 +1, 최대값을 갱신

# 2. 시간복잡도 
# BFS = O(V+E)  V = M * N, E = V * 4

# 3. 자료구조 
# 그래프 전체 지도  : INT[][]
# 방문 : bool[][]
# 큐(bfs)


import sys
input= sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split()))for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]



def bfs(y,x):
    rs= 1

    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0 <= nx <m:
                if map[ny][nx]== 1 and chk[ny][nx] == False:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

            
            
            


cnt = 0
maxy= 0

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] ==False:
            chk[j][i] = True
            # 전체 그림 +1
            cnt += 1
            # BFS > 크기 구해주고
            maxy = max(maxy, bfs(j,i))
            # 최대값 갱신

print(cnt)
print(maxy)