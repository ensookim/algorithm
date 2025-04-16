T = int(input())

for t in range(1, T+1):
    number = map(int, input().split())
    addnum = sum(num for num in number if num%2 != 0)
    print(f"#{t} {addnum}")



