# Given a string s, find the length of the longest substring without repeating
# characters.

def lengthOfLongestSubstring(s: str) -> int:

    # Optimized solution
    # We consider a set as it does not store duplicates and search time is
    # linear. We then consider the sliding window concept where we form
    # the substring using l,r pointers and in case we encounter a duplicate
    # in the range, we start increasing the left index and we do this til
    # there is no dupl in the set and we calc the max value of substring

    result_set = set()
    left = 0
    value = 0
    for right in range(len(s)):
        while s[right] in result_set:
            result_set.remove(s[left])
            left += 1
        result_set.add(s[right])
        value = max(value, right-left+1)
    return value

    # Working solution-1
    # if len(s) > 0:
    #     result_set = set([])
    #     val = 1
    #     for left in range(len(s)):
    #         result_set.add(s[left])
    #         for r in range(left+1, len(s)):
    #             if s[r] not in result_set:
    #                 result_set.add(s[r])
    #                 val = max(len(result_set), val)
    #             else:
    #                 break
    #         result_set.clear()
    #     return val
    # else:
    #     return 0

    # Try-1
    # if len(s) > 0:
    #     result_set = {s[0]}
    #     val = 1
    #     left, right = 0, 1
    #     while right < len(s):
    #         if s[left] != s[right] and s[right] not in result_set:
    #             result_set.add(s[right])
    #             right += 1
    #             val = max(len(result_set), val)
    #         else:
    #             # n = len(result_set)
    #             # val = max(n, val)
    #             result_set.clear()
    #             result_set.add(s[right])
    #             left = right
    #             right += 1
    #     return val
    # else:
    #     return 0


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("aab"))
print(lengthOfLongestSubstring("au"))
