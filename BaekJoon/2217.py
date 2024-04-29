#로프

n = int(input())
rope = []

for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)
result = []


for j in range(n):
    result.append(rope[j]* (j+1))

print(max(result))
