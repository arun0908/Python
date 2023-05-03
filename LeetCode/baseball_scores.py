# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x: Record a new score of x.
# '+': Record a new score that is the sum of the previous two scores.
# 'D': Record a new score that is the double of the previous score.
# 'C': Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the
# operations.


def calPoints(operations: list[str]) -> int:
    stack = []
    for o in operations:
        if o == "+":
            stack.append(stack[-1] + stack[-2])
        elif o == "D":
            stack.append(stack[-1]*2)
        elif o == "C":
            stack.pop()
        else:
            stack.append(int(o))
    return sum(stack)


print(calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # 27
print(calPoints(["5", "2", "C", "D", "+"]))  # 30
