# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.

def generateParenthesis(n: int) -> list[str]:
    stack = []
    res = []

    def track_parantheses(open, closed):
        if open == closed == n:
            res.append("".join(stack))
            return
        if open < n:
            stack.append("(")
            track_parantheses(open + 1, closed)
            stack.pop()
        if closed < open:
            stack.append(")")
            track_parantheses(open, closed + 1)
            stack.pop()
    track_parantheses(0, 0)
    return res


print(generateParenthesis(3))
