# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character.
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter
# you can get after performing the above operations.

def characterReplacement(s: str, k: int) -> int:
    value_map = {}
    result = 0
    left = 0
    for right in range(len(s)):
        if s[right] not in value_map:
            value_map[s[right]] = 0
        value_map[s[right]] += 1
        window_length = right-left+1
        max_freq = max(value_map.values())
        if window_length-max_freq <= k:
            result += 1
        else:
            value_map[s[left]] = value_map[s[left]]-1
            left += 1
    return result

    # 1st try
    # result = 0
    # temp_list = []
    # for l in range(len(s)):
    #     i = k
    #     for r in range(0, len(s)):
    #         if s[l] != s[r] and i>0:
    #             temp_list.append(s[l])
    #             i -= 1
    #         elif s[l] == s[r] and i>0:
    #             temp_list.append(s[r])
    #     result = max(result, len(temp_list))
    #     temp_list.clear()
    # return result


print(characterReplacement("ABAB", 2))  # 4
print(characterReplacement("AABABBA", 1))  # 1
