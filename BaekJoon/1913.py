N = int(input())
target = int(input())

matrix = [[0] * N for _ in range(N)]

# 방향을 설정 (상, 우, 하, 좌)
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

i, j = N // 2, N // 2
matrix[i][j] = 1

move = 0  # 방향 인덱스
num = 2  # 시작 숫자
steps = 1  # 한 방향으로 이동할 횟수
target_position = (i + 1, j + 1) if target == 1 else None  # 타겟 좌표 저장 (1부터 시작하는 좌표)

# 나선형으로 숫자를 채우기
while num <= N * N:
    for direction in range(4):  # 상, 우, 하, 좌 순서로 방향 전환
        for _ in range(steps):
            # 다음 위치 계산
            i += di[direction]
            j += dj[direction]

            # 숫자 채우기
            matrix[i][j] = num

            # 타겟 숫자의 위치 저장
            if num == target:
                target_position = (i + 1, j + 1)  # 문제에서 요구한 좌표는 1부터 시작

            num += 1
            if num > N * N:
                break

        # 두 방향마다 step을 증가시켜야 함
        if direction % 2 == 1:
            steps += 1

# 결과 출력
for row in matrix:
    print(" ".join(map(str, row)))

# 타겟 숫자의 좌표 출력
if target_position:
    print(f"타겟 위치: {target_position}")
