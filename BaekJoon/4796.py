case = 1
while(True):

    L,P,V = map(int,input().split())
    if (L,P,V) == (0,0,0):
        break
    else:


        week = V//P
        day = V%P
        if day > L:
            print(f"Case {case}: {week*L + L}")

        else:
            print(f"Case {case}: {week*L + day}")
        case += 1





