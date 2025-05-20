# 13460 구슬탈출 2
# 직사각형 보드, 빨강, 파랑 구슬 넣고 빨강구슬 탈출 시키기
# 세로 N, 가로M
# 구멍 -> 파란구슬 들어가면 X, 동시에 들어가도 X, 같은 칸 X
# 왼쪽, 오른쪽, 위, 아래


# 입력
# 5 5
# #####
# #..B#
# #.#.#
# #RO.#
# #####

# 출력
# 빨간 구슬이 구멍에 들어갈 최소 움직임
# 뺄 수 없으면 -1

# 1. 초기 상태: (빨강X, 빨강Y, 파랑X, 파랑Y, depth = 0)
# 2. visited에 (rX, rY, bX, bY) 저장해 중복 막기
# 3. 큐에 현재 상태를 넣고 BFS 시작
# 4. 4방향으로 기울여봄:
#     - move(red), move(blue)
#     - 파란색이 구멍에 들어가면 → 실패
#     - 빨간색만 들어가면 → 성공 → depth + 1 리턴
#     - 겹치면 움직인 거리 비교해서 한 칸 뒤로
#     - visited에 없으면 → 큐에 넣기
#
# 5. depth > 10 이면 실패
# 6. 큐 다 돌 때까지 위 반복



from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]


# 이동하는 함수
# 다음칸이 벽이 아니고, 지금 칸이 구멍이 아니면
# 한칸씩 이동하고 cnt +=1
# return x, y, cnt
def move(x, y, dx, dy, board):
    count = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        y += dy
        x += dx
        count += 1
    return x,y,count



# BFS (10번까지)
# 빨, 파 구슬 찾고
# 초기상태 넣고
# 방문처리하고
# 굴리고  방문처리 반복
def solve(board, n, m):
    visited = set()
    queue = deque()

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i ,j
            elif board[i][j] == 'B':
                bx, by = i,j
    # 찾은 위치 큐에 넣고 방문처리
    queue.append((rx,ry,bx,by,0))
    visited.add((rx,ry,bx,by))

    #BFS 시작
    while queue:
        rx,ry,bx,by,depth = queue.popleft()
        if depth >= 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx,ry,dx[i],dy[i],board)
            nbx, nby, bc = move(bx,by,dx[i],dy[i],board)

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                return depth+1


            # 겹치면 굴린 횟수가 많은 거 -i
            if nrx == nbx and nry == nby:
                if rc>bc:
                    nrx -= dx[i]
                    nry -= dy[i]

                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx,nry, nbx,nby) not in visited:
                visited.add((nrx,nry,nbx,nby))
                queue.append((nrx,nry,nbx,nby,depth+1))

    return -1




# 입력
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

print(solve(board, n, m))





