T = int(input())
for i in [300,60,10]:
    if T % 10 !=0:
        print(-1)
        break
    else:
        print(T//i , end=' ')
        T = T%i

