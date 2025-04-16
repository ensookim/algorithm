
for t in range(int(input())):
    word = input()
    for i in range(1,10): #마디가 최대 10글자니까
        if word[:i] == word[i:2*i]: # 미쳐따
            print(f'#{t+1} {i}')
            break
        