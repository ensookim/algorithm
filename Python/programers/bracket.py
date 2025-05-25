def is_valid(s):
    stack = []
    bracket = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket.values():
            stack.append(char)
        elif char in bracket:
            if not stack or stack[-1] != bracket[char]:
                return False
            stack.pop()
    return not stack

def solution(s):
    answer = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            answer += 1
    return answer
