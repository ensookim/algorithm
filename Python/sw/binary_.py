def binary_s(target, array):
    cur_min = 0
    cur_max = len(array) -1
    cur_guess = cur_min + cur_max // 2
    
    while cur_min <= cur_max:
        if array[cur_guess] == target:
            return True
        elif array[cur_guess] < target:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess -1
        cur_guess = cur_min + cur_max // 2
    


# 

def binary_search(target, array):
    sorted_arr= sorted(array)
    # 정렬 후 이분탐색 시작
    cur_min = 0 
    cur_max = len(sorted_arr)-1
    cur_pointer = (cur_min + cur_max) //2
    
    while cur_min <= cur_max:
        if sorted_arr[cur_pointer] == target:
            return True
        elif sorted_arr[cur_pointer] < target:
            cur_min = cur_pointer+1
        else:
            cur_max = cur_pointer-1
        cur_pointer = (cur_min + cur_max) //2
        print(sorted_arr)
    
    

arr =[0, 3, 5, 6, 1, 2, 4]
print(binary_search(2,arr))