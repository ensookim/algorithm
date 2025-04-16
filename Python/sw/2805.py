T = int(input())  # 테스트 케이스 개수 입력

for t in range(1, T + 1):
    N = int(input())
    map = [list(map(int, input())) for _ in range(N)]
    j = N // 2
    count = 0

    print(map)

    for k in range(N):
        if k <= N // 2:  # 위쪽 삼각형 부분 (가운데를 포함)
            count += sum(map[k][j-k:j+k+1])
        else:
            count += sum(map[k][j-(N-k-1)//2:j+(N-k-1)//2+1])

    print(count)

