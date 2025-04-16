
import sys
input = sys.stdin.readline



def Solv(N, water):
    water.sort()
    left = 0
    right = N-1
    closest_sum = float('inf') 
    
    best = (0,0)
    
    while left < right:
        current_sum = water[left] + water[right]
        
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            best = (water[left], water[right])
            
        if current_sum < 0:
            left += 1
            
        elif current_sum > 0:
            right -= 1
        else:
            break
    

    return tuple(sorted(best))


N = int(input())
water = list(map(int, input().split()))

result = Solv(N, water)
print(result[0], result[1])
    
    