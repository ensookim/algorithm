# push x => int x 를 스택에 넣음

import sys
input =sys.stdin.readline

i = int(input())
stack = []
for i in range(i):
    comment = input()
    if comment.startswith('push'):
        _,x = comment.split()
        stack.append(int(x))
    elif comment.startswith('pop'):
        if stack:
            print(stack.pop())
        else:
            print(-1)
        
    elif comment.startswith('size'):
        print(len(stack))
    elif comment.startswith('empty'):
        if stack:
            print(0)
        else:
            print(1)
    elif comment.startswith("top"):
        if stack:
            print (stack[-1])
        else:
            print(-1)
# n = int(input())


# for _ in range(n):
#     command = input().split()

#     if command[0] == "push":
#         stack.append(int(command[1]))
#     elif command[0] == "pop":
#         print(stack.pop() if stack else -1)
#     elif command[0] == "size":
#         print(len(stack))
#     elif command[0] == "empty":
#         print(0 if stack else 1)
#     elif command[0] == "top":
#         print(stack[-1] if stack else -1)



        



