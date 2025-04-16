def bubble_sort(array):
    
    for i in range(len(array)-1):
        for j in range(len(array) -i - 1):
            if array[j] > array[j+1]:
               array[j], array[j+1] =array[j+1],array[j]
               print(array)
    
    return array

def select_sort(array):
    
    for i in range(len(array)-1):
        min_index = i
        for j in range(len(array)-i):
            if array[i +j] < array[min_index]:
                min_index = i +j 
        
        array[i], array[min_index] = array[min_index], array[i]
        
        


def insrtion_sort(array):
    for i in range(1,len(array)):
        for j in range(i):
            if array[i - j] <array[i - j -1]:
                array[i - j] ,array[i - j -1] = array[i - j -1],array[i - j]
            
            else:
                break
    return array

arr  = [8,21,32,4,0,1,2]
print(bubble_sort(arr))