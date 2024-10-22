def average(num=[]):
    result_average = 0
    for i in num:
        result_average += i  
    
    return round(result_average / len(num))

T = int(input())

for t in range(1, T + 1):
    number = list(map(int, input().split())) 
    result = average(number)
    print(f"#{t} {result}") 
