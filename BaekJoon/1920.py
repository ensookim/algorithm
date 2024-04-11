def check(N, A, M, num_list):
        num_set = set(A)

        for i in num_list:
         if i in num_set:
             print("1")  
         else:
            print("0")  


N = int(input())
A = list(map(int, input().split()))
M = int(input())
num_list = list(map(int, input().split()))

check(N, A, M, num_list)
