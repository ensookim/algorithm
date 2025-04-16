n = int(input())
x, y = 1, 1
plan = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for p in plan:
    for i in range(len(move_type)):
        if p == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 새로운 위치가 범위를 벗어나지 않는지 확인
            if 1 <= nx <= n and 1 <= ny <= n:
                x, y = nx, ny
                break  # 유효한 이동이 확인되면 더 이상 반복하지 않음

print(x, y)
