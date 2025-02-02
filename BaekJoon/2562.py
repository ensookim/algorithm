# 최대값

# 9개의 다른 수 주어짐
# 최대 값 출력, 몇 번쨰 인댁스인지

def MaxReturn(num):

    maxnum= num[0]
    whereMaxnum = 0 
    
    for i in range(len(num)):
        if maxnum < num[i]:
            maxnum = num[i]
            whereMaxnum = i

    return maxnum, whereMaxnum
    
    
    
num =[]
for i in range(9):
    num.append(int(input()))

maxnum, whereMaxnum = MaxReturn(num)

print(maxnum)
print(whereMaxnum+1)