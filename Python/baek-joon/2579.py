step = int(input(""))
point = []
result = [0] * step  # 최대 점수를 저장할 리스트

# 계단 점수 입력받기
for i in range(step):
    point.append(int(input()))

# 점수 계산 
# 하나 둘일땐 정해져있음


if step == 1:
    result[0] = point[0]
    
elif step == 2:
    result[1] = point[0] + point[1]
    
else:  # 3개부터 
    
    result[0] = point[0]
    result[1] = point[0] + point[1]
    result[2] = max(point[1] + point[2], point[0] + point[2]) # 1 2, 0 2 
    
    
    for i in range(3, step+1): # 4개 부터, 
        result[i] = max(point[i] + result[i-2], result[i-3] + point[-1]+ point[i])
         

print(result[-1])
