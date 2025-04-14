# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

import sys



def dfs(idx) :
    global visited
    visited[idx] =True
    print(idx, end= ' ')
    for next in range(1, N +1 ):
        if not visited[next] and graph[idx][next]:
            dfs(next)


def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end= ' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] =True
                q.append(next)

input =sys.stdin.readline


N, M, V = map(int, input().split())
visited =[False] * (N +1)
graph= [[False] * (N +1) for _ in range(N+1)]
# 1. 그래프 정보입력

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True



# 2. dfs

dfs(V)
print()


# 3. bfs
visited =[False] * (N +1)

q = [V]
visited[V] = True
bfs()
