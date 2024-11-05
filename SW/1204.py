from collections import Counter

# 최 빈수는 가장 많이 분포하는 값
# 여러개일땐 가장 큰 점수
# 0~100 값 1000명
T = int(input())

for t in range(T):
    num = int(input())
    nlist = map(int, input().split())
    count = Counter(nlist)
    most_common_count = count.most_common()
    # print(most_common_count)

    max_frequency = most_common_count[0][1]
    most_frequent_values = [item[0] for item in most_common_count if item[1] == max_frequency]
    max_frequency_value = max(most_frequent_values)
    print(f"#{t+1} {max_frequency_value}")

