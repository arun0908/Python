# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def validPalindrome(s: str) -> bool:
    # take two pointers for left and right and iterate through string
    l , r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            # take two strings, one where we ignore left char, one where we ignore right char and check if either are same
            # we take r+1 for left as we need to consider even the last char, same for r, we ignore last char as per logic
            skipl, skipr = s[l+1: r+1] , s[l: r]
            return (skipl == skipl[::-1] or skipr == skipr[::-1])
        l , r = l+1, r-1
    return True

print(validPalindrome("abca"))
        