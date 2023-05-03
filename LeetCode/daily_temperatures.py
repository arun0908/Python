"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to
wait after the ith day to get a warmer temperature. If there is no future day
for which this is possible, keep answer[i] == 0 instead.
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    None
    """
    # Initial approach
    # answer = []
    # for i in range(len(temperatures)):
    #     r = i + 1
    #     while r<len(temperatures) and temperatures[i]>=temperatures[r]:
    #         r += 1
    #     if r<len(temperatures) and temperatures[i] < temperatures[r]:
    #         answer.append(r-i)
    #     else:
    #         answer.append(0)
    # return answer

    # Optimized solution:
    answer = [0] * len(temperatures)
    my_stack = []
    for idx, value in enumerate(temperatures):
        while my_stack and value > my_stack[-1][1]:
            stack_value = my_stack.pop()
            answer[stack_value[0]] = idx - stack_value[0]
        my_stack.append([idx, value])
    return answer


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
