# 동전 0

# 최소 동전

n, k  =map(int, input().split())
result = 0

coins = []
for i in range(n):
    coins.append(int(input()))
   
coins.sort(reverse=True)



for i in coins:
    result += k // i
    k %= i
     
print(result)