# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

def isUgly(n: int) -> bool:
    while n > 1:
        if (n % 2) == 0:
            n = int(n/2)
        elif (n % 3) == 0:
            n = int(n/3)
        elif (n % 5) == 0:
            n = int(n/5)
        else:
            return False
    return n == 1


print(isUgly(6))  # true
print(isUgly(14))  # false
