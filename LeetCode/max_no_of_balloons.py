# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

from collections import Counter


def maxNumberOfBalloons(text: str):
    balloon = Counter("balloon")
    text_map = Counter(text)
    result = float("inf")
    for c in balloon:
        result = min(result, text_map[c]//balloon[c])
    return result
    # balloon = {}
    # text_map = {}
    # for c in "balloon":
    #     balloon[c] = 1 + balloon.get(c,0)
    # for c in text:
    #     text_map[c] = 1 + text_map.get(c,0)
    # result = len(text)
    # for c in balloon:
    #     result = min(result, text_map[c]//balloon[c])
    # return result


print(maxNumberOfBalloons("leetcode"))  # 0
print(maxNumberOfBalloons("nlaebolko"))  # 1
