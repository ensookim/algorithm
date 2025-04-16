from collections import deque

def is_correct_parenthesis(string):
    stack = []
    
    for char in string:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    else: 
        return change_to_correct_parentheses(balanced_parentheses_string)


def change_to_correct_parentheses(balanced_parentheses_string):
    if balanced_parentheses_string == "":
        return ""
    
    u, v = separate_to_u_v(balanced_parentheses_string)
    
    if is_correct_parenthesis(u):
        return u + change_to_correct_parentheses(v)
    else:
        return "(" + change_to_correct_parentheses(v) + ")" + revers_parentheses(u[1:-1])


def separate_to_u_v(string):
    q = deque(string)
    left_count, right_count = 0, 0
    u, v = "", ""

    while q:
        char = q.popleft()
        u += char
        if char == "(":
            left_count += 1
        elif char == ")":
            right_count += 1

        if left_count == right_count:
            break

    v = ''.join(q)
    return u, v


def revers_parentheses(string):
    revers_string = ""
    for char in string:
        if char == "(":
            revers_string += ")"
        elif char == ")":
            revers_string += "("
    return revers_string


# 테스트
print(get_correct_parentheses("()))((()"))  # "()(())()"가 반환되어야 함

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()() / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))
