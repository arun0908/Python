def evalRPN(tokens: list[str]) -> int:
    if len(tokens) == 1:
        return int(tokens[-1])
    value_list = [int(tokens[0]), int(tokens[1])]
    for c in tokens[2:]:
        if c in '+-*/':
            if c == '+':
                b, a = value_list.pop(), value_list.pop()
                value_list.append(a+b)
            elif c == '-':
                b, a = value_list.pop(), value_list.pop()
                value_list.append(a-b)
            elif c == '*':
                b, a = value_list.pop(), value_list.pop()
                value_list.append(a*b)
            else:
                b, a = value_list.pop(), value_list.pop()
                value_list.append(int(a/b))
        else:
            value_list.append(int(c))
    return value_list[-1]

    # Initial Approach:

    # if len(tokens) == 1:
    #         return int(tokens[-1])
    # value_list = []
    # for c in tokens:
    #     if c == '+':
    #         temp= value_list[-2] + value_list[-1]
    #         value_list.pop()
    #         value_list.pop()
    #         value_list.append(temp)
    #     elif c == '-':
    #         temp= value_list [-2] - value_list[-1]
    #         value_list.pop()
    #         value_list.pop()
    #         value_list.append(temp)
    #     elif c == '*':
    #         temp= value_list [-2] * value_list[-1]
    #         value_list.pop()
    #         value_list.pop()
    #         value_list.append(temp)
    #     elif c == '/':
    #         temp= value_list [-2] / value_list[-1]
    #         value_list.pop()
    #         value_list.pop()
    #         value_list.append(int(temp))
    #     else:
    #         value_list.append(int(c))
    # return value_list[-1]


print(evalRPN(["2", "1", "+", "3", "*"]))  # 9
print(evalRPN(["4", "13", "5", "/", "+"]))  # 6
