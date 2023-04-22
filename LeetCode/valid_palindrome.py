# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.


def isPalindrome(s: str) -> bool:
    # Method utilizing O(n) time, but extra space

    # newstr = ""
    # for c in s:
    #     if c.isalnum():
    #         newstr += c.lower()
    # return newstr == newstr[::-1]

    # O(n) solution and O(1) space with no extra space

    l, r = 0, len(s)-1
    while l < r:
        while l < r and not alphanumeric(s[l]):
            l += 1
        while r > l and not alphanumeric(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def alphanumeric(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


print(isPalindrome("0P"))  # False
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
