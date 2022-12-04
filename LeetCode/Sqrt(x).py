# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer
# should be non-negative as well. You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


def mySqrt(x: int) -> int:
    if 0 <= x <= 1:
        return x
    l, r = 0, x
    while l <= r:
        mid = (r + l) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif x < mid * mid:
            r = mid
        else:
            l = mid + 1


print(mySqrt(4))  # 2
print(mySqrt(8))  # 2.8 = 2
