N = int(input())
time = list(map(int, input().split()))
result = 0
current_sum = 0
time.sort()

for t in time:
    current_sum += t
    result += current_sum

print(result)
