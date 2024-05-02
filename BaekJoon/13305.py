

n = int(input()) 
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
minPrice=price[0]
total=0

for i in range(n-1):
    if minPrice>price[i]:
        minPrice=price[i]

    total+=(minPrice*distance[i])

print(total)


