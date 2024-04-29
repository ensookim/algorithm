# 코인 500 100 50 10 5 1
# 1000원으로 
# 리스트 넣고 검사하면서 1씩 카운트
n = 1000 - int(input())
coins = (500,100,50,10,5,1)
count = 0
for coin in coins:
    count += n//coin
    n%=coin
print(count)