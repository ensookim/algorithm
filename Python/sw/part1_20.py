def is_valid_date(year, month, day):
    if month < 1 or month > 12:
        return False

    
    max_days = {
        1: 31,  
        2: 28,
        3: 31,  
        4: 30,  
        5: 31,  
        6: 30,  
        7: 31,  
        8: 31,  
        9: 30,  
        10: 31, 
        11: 30, 
        12: 31  
    }

    return 1 <= day <= max_days[month]

def format_date(year, month, day):
    return f"{year:04d}/{month:02d}/{day:02d}"



if __name__ == '__main__': 
   
    T = int(input())
 
    for t in range(1, T+1):
        
        date_input = input()
        if len(date_input) != 8 or not date_input.isdigit():
            print(f"#{t} -1")
            continue
        
        year = int(date_input[:4])
        month = int(date_input[4:6])
        day = int(date_input[6:8])
        
        if is_valid_date(year, month, day):
            print(f"#{t} {format_date(year, month, day)}") 
        else:
            print(f"#{t} -1")
