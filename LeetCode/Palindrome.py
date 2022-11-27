# Given an integer x, return true if x is a palindrome, and false otherwise.
def isPalindrome(self, x: int) -> bool:
    # Generic solution
    # if x == 0:
    #     return True
    # temp = 0
    # temp_x = x
    # while temp_x > 0:
    #     temp = temp * 10 + temp_x % 10
    #     temp_x = temp_x // 10
    # return x == temp

    # One line solution using string methods
    if x < 0:
        return False
    return str(x) == str(x)[::-1]
