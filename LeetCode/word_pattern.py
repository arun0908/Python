# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

def wordPattern(pattern: str, s: str) -> bool:
    pattern_map = {}
    string_map = {}
    s1 = s.split()
    if len(pattern) != len(s1):
        return False
    # for i in range(len(s)):
    #     c , w = pattern[i],s[i]
    for c, w in zip(pattern, s1):
        if (c in pattern_map and pattern_map[c] != w) or (w in string_map and string_map[w] != c):
            return False
        pattern_map[c] = w
        string_map[w] = c
    return True


print(wordPattern("abba", "dog cat cat dog"))  # True
print(wordPattern("abba", "dog cat cat fish"))  # False
print(wordPattern("aaaa", "dog cat cat dog"))  # False
