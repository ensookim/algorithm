T = int(input())  # 테스트 케이스 개수

for t in range(T):
    N = int(input())  # 파스칼 삼각형의 크기
    triangle = [[1] * (i + 1) for i in range(N)]  # 파스칼 삼각형을 위한 2D 리스트 초기화

    # 각 줄에 대해 계산
    for i in range(2, N):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    print(f"#{t}")
    # 파스칼 삼각형 출력
    for row in triangle:
        print(" ".join(map(str, triangle[i])))
