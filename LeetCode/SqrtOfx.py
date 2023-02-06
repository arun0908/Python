# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer
# should be non-negative as well. You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Use binary search to check from 0 to the number and if the number lies in between the range of mid and mid + 1 squared, then that is our answer
def mySqrt(x: int) -> int:
    if 0 <= x <= 1:
        return x
    l, r = 0, x
    ans = 0
    while l <= r:
        mid = (r + l) // 2
        # First approach
        # if mid * mid <= x < (mid + 1) * (mid + 1):
        #     return mid
        # elif x < mid * mid:
        #     r = mid
        # else:
        #     l = mid + 1
        if (mid*mid) > x:
            r = mid - 1
        elif (mid * mid) < x:
            ans = mid
            l = mid + 1
        else:
            return mid
    return ans

# Continuation of the problem, to find out even the float part upto a specified limit to round up


def preciseSqrt(x: int, round_up: int):
    ans = mySqrt(x)
    factor = 1
    for i in range(1, (round_up+1)):
        factor = factor/10
        j = ans
        while (j*j) < x:
            j += factor
        ans = j - factor
    return ans


# print(mySqrt(4))  # 2
print(preciseSqrt(8, 2))  # 2.8 = 2
print(preciseSqrt(101, 2))
print(preciseSqrt(37, 3))
