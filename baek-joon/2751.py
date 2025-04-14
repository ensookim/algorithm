import sys
input =sys.stdin.readline

list=[]
N = int(input())    
for i in range(N):
    list.append(int(input()))
list.sort(reverse=False)
for  i in list:
    print(i)
    
    