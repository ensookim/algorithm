import heapq

def maximize_jewel_value(n, k, jewels, bags):
    # 보석을 무게 기준으로 정렬
    jewels.sort()
    # 가방을 무게 기준으로 정렬
    bags.sort()

    max_value = 0
    max_heap = []
    jewel_index = 0

    # 가방에 대해 탐색
    for bag_capacity in bags:
        # 가방 무게보다 작거나 같은 보석을 최대 힙에 추가
        while jewel_index < n and jewels[jewel_index][0] <= bag_capacity:
            heapq.heappush(max_heap, -jewels[jewel_index][1])  # 가격을 음수로 삽입 (최대 힙처럼 사용)
            jewel_index += 1

        # 힙에서 가장 비싼 보석을 선택
        if max_heap:
            max_value -= heapq.heappop(max_heap)

    return max_value


# 입력 처리
n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

# 결과 출력
print(maximize_jewel_value(n, k, jewels, bags))
