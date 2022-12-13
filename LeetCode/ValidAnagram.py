# Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or phrase
# formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.

def isAnagram(s: str, t: str) -> bool:
    # First approach, but this takes a space and time complexity of O(s+t)
    if len(s) != len(t):
        return False
    s_map, t_map = {}, {}
    for i in range(len(s)):
        s_map[s[i]] = 1 + s_map.get(s[i], 0)
        t_map[t[i]] = 1 + t_map.get(t[i], 0)
    for c in s_map:
        if s_map[c] != t_map.get(c,0):
            return False
    return True
    # Second approach would be to use sorted method for sorting and then compare both the strings.
    # return sorted(s) == sorted(t)


print(isAnagram("reed", "deer"))
