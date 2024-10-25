for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    weight.sort()
    
    left = 0 
    right = len(weight) -1 
    max_weight = -1 

    while left < right:
        result = weight[left] + weight[right]
        
        if result > m:
            right -= 1
        
        else:
            max_weight = max(result, max_weight)
            left +=1 
            
    print(f"#{t} {max_weight}")
    
    
    
    

    