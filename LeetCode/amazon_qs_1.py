"""
There are n developers working at Amazon where the th developer has the
experience points experience[i]. The company decided to pair the developers by
iteratively pairing the developers with the highest and lowest remaining
experience points for a hackathon. The combined experience of a pair is the
average of the experience points of the two developers. Find the number of
unique values among the combined experience of the pairs formed.
"""


def unique_pairs(list1: list[int]) -> int:
    """
    Determine unique pairs
    """
    list1.sort()
    res = set()
    left, right = 0, len(list1) - 1
    while left < right:
        avg = (list1[left] + list1[right]) / 2
        if avg not in res:
            res.add(avg)
        left += 1
        right -= 1
    return len(res)


print(unique_pairs([1, 100, 10, 1000]))  # 2
print(unique_pairs([1, 4, 1, 3, 5, 6]))  # 2
