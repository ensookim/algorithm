def find_max_plus_or_multiply(array):
    find_max_plus_or_multiply_sum = 0
    
    for number in array:
        if number <= 1 or find_max_plus_or_multiply_sum <= 1:
            find_max_plus_or_multiply_sum += number
        else:
            find_max_plus_or_multiply_sum *= number
    return find_max_plus_or_multiply_sum




result = find_max_plus_or_multiply

