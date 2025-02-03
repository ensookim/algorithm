def palindrome(string):

    
    for i in range(len(string)):
        if string[i] == string[len(string)-1 - i]:
            return True
        else:
            return False
        
    
def recursive_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    return recursive_palindrome(string[1:-1])