# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Stack:
#     def __init__(self):
#         self.head = None

#     def push(self, value):
#         new_head = Node(value)
#         new_head.next= self.head
#         self.head = new_head
        

#     # pop 기능 구현
#     def pop(self):
#         delete_head = self.head
#         self.head = self.head.next
#         return delete_head.data

#     def peek(self):
#         return self.head.data

#     # isEmpty 기능 구현
#     def is_empty(self):
#         return self.head is None    
    


def solution(arr):  
    answer = [0] * len(arr) # 0 0 0 0 
    for i in range(len(arr)-1, 0, -1):
        for j in range(i -1, -1 ,-1):
            if arr[i] <= arr[j]:
                answer[i] = j +1
                break
    return answer


def stack_solution(arr):
    answer = [0] * len(arr) # 0 0 0 0 
    while arr:
        top = arr.pop()
        for  i in range(len(arr)-1, -1, -1): # 4 3 2 1 
            if arr[i] >= top : # arr의 4
                answer[len(arr)] =  i +1
                break
            
    return answer