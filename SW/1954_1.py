# 달팽이 DP
from docutils.utils.math.latex2mathml import mover
from patsy.eval import test_ast_names
from sympy.integrals.manualintegrate import tansec_seceven

# 입력 T 받고
# 우 하 좌 상 우

# 만약 좌 하 상 우
# 방향배열, modv , x , y


T = int(input())

di = [-1,0,1,0]
dj = [0,1,0,-1]

for testCase in range(1,T+1):

    move =  0
    N =int(input())
    i , j = int(N/2), int(N/2)
    mat = [[0]*N for _ in range(N)]

    for k in range(1,N*N+1): # 배열 돌면서 좌표 확정하고 다음 값 넣어줌

        mat[i][j] = k

        ni = i + di[move]
        nj = j + dj[move]

        # 조건확인  조건 : 다음값이 ==0 이고 범위(0<= ni <N 내에 있어야함)

        if 0 <= ni < N and 0 <= nj < N and mat[ni][nj] == 0:
            i ,j = ni,nj

        else:

            move = (move+1)%4
            i = i + di[move]
            j = j + dj[move]



    print(f"#{testCase}")
    for row in mat:
        print(*row)



