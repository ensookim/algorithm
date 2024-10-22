
def min_operations_to_exceed_N(A, B, N):
    operations = 0
    while A <= N and B <= N:
        if A < B:
            A += B
        else:
            B += A
        operations += 1
    return operations

# 입력 받기
T = int(input())  # 첫 줄에 테스트 케이스의 수

for _ in range(T):
    A, B, N = map(int, input().split())
    print(min_operations_to_exceed_N(A, B, N))

