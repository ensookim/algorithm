def revers_word(string):
    count_all_zero = 0
    count_all_one = 0
    
    
    if string[0] == 0:
        count_all_one += 1
    else:
        count_all_zero += 1
        
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i] == '0':
                count_all_zero += 1
            else:
                count_all_one += 1
                
    
    return min(count_all_one, count_all_zero)


