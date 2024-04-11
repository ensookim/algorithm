# ATM 


n = int(input())
people = list(map(int, input().split()))
people.sort()
answer= 0

for i in range(1, n+1):
    answer = answer + sum(people[:i])
    

print(answer)