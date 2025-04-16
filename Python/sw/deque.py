from collections import deque




def count_nasdaq(price):
    result = [0] * len(price)
    for i in range(len(price)-1):
        count = 0
        for j in range(i+1, len(price)):
            if price[i] <= price[j]:
                count += 1 
            else:
                count += 1
                break
        result[i] =count
    return result
            

def q_count(price):
    result = []
    q = deque(price)
    
    while q: #q 가 비어있지않다면
        count =0
        current_price=  q.popleft()
        for next in q:
            if current_price <= next:
                count += 1
            else:
                count += 1
                break
        result.append(count)
    return result
               




a = [2,1,4,2,7]

print(q_count(a))