# 입력
from nltk import Model

T = int(input())
# 방향

di = [0,1,0,-1]
dj = [1,0,-1,-0]
for t in range(1,T+1):
    N = int(input())
    mat = [[0]*N for _ in range(N)]
    i, j , move = 0 ,0 ,0

    for k in range(1,N*N+1):
        mat[i][j] = k
        ni ,nj = i + di[move], j + dj[move]

        if 0 <= ni < N and 0 <= nj < N and mat[ni][nj] == 0:
            i, j = ni,nj


        else:
            move = (move + 1) % 4
            i , j = i+di[move], j+dj[move]


    for row in mat:
        print(*row, sep=" ")


# if문

