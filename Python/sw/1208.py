for testCase in range(1, 11):  # 1부터 10까지 테스트 케이스 실행
    dump = int(input())  # 덤프 횟수 입력
    box = list(map(int, input().split()))  # 박스 높이 입력

    for i in range(dump):
        box.sort(reverse=True)  # 박스 리스트를 내림차순 정렬
        box[0] -= 1  # 가장 높은 박스의 높이를 1 줄임
        box[-1] += 1  # 가장 낮은 박스의 높이를 1 늘림

        # 평탄화 확인
        if box[0] - box[-1] <= 1:
            break

    maxResult = max(box) - min(box)
    print(f"#{testCase} {maxResult}")

