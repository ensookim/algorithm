N = int(input())

for n in range (1, N+1):
    ans_str = str(n)
    ans_str = ans_str.replace('3', '-')
    ans_str = ans_str.replace('6', '-')
    ans_str = ans_str.replace('9', '-')

    if '-' in ans_str:
        for i in range(10):
            ans_str = ans_str.replace(f'{i}', '')

    print(ans_str, end = ' ')
