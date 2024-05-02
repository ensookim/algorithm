import heapq
import sys
input = sys.stdin.readline

n = int(input())  # 뭉치 개수
nums = []  # 우선순위 큐
result = 0

for _ in range(n):
    heapq.heappush(nums, int(input()))  # 각 카드 뭉치 우선순위 큐 삽입

if len(nums) == 1:  
    print(0)
else:  # 2개 이상의 카드 뭉치가 있다면
    while nums:  # 카드 뭉치가 있을 동안
        if len(nums) == 2:  
            print(result + sum(nums))  # 결과 출력 후 반복문 종료
            break
        temp = heapq.heappop(nums) + heapq.heappop(nums)  
        heapq.heappush(nums, temp) 
        result += temp  