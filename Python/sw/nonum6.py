def sol(N, Action):
    answer = ''
    cl = False
    for action in Action:
        if action == "CL":
            cl = not cl
        elif action == "BS":
            if answer:
                answer = answer[:-1]
        else:
            if cl:
                answer += action.swapcase()
            else:
                answer += action
    return answer



Action= ["h","CL", "e","l","l","BS"]

print(sol(6, Action))

