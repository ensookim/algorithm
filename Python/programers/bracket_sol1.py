

def is_valid(s):
    stack= []
    bracket = {']':'[','}':'{',')':'('}

    for c in s:
        if c in bracket.values():
            stack.append(c)
        elif c in bracket:
            if not stack or stack[-1] != bracket[c]:
                return False
            stack.pop()
    return not stack


def solution(s):
    answer =0
    for i in range(len(s)):
        rotated = s[i:] +s [:i]
        if is_valid(rotated):
            answer += 1
    return answer

