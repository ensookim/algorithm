
def maxff(sel,boom):
    step= 0
    for i in range(1,sel+1):
        if step+i == boom:
            continue
        else:
            step+=i

    return step

T = int(input())

for testCase in range(1, T + 1):
    a, b = map(int, input().split())
    print(maxff(a, b))
