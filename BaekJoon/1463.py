def min_operations_to_one(N):
    dp = [0] * (N + 1)

    for i in range(2, N + 1):
        # 1을 빼는 경우
        dp[i] = dp[i - 1] + 1

        # 2로 나누는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # 3으로 나누는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[N]

N = int(input())
result = min_operations_to_one(N)
print(result)