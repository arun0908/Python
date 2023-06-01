"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has
piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses
some pile of bananas and eats k bananas from that pile. If the pile has less
than k bananas, she eats all of them instead and will not eat any more bananas
during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas
before the guards return.
Return the minimum integer k such that she can eat all bananas within h hrs.
"""

import math


def min_eating_speed(piles: list[int], h: int) -> int:
    """
    Search the minimum eating speed using binary search
    """
    # Find the number of optimum bananas by using binary search. We consider
    # the range by taking into account that the total number of piles in the
    # input list will always be greater than or equal to h and that the max
    # speed would be the max number of pile in the list. we then check for
    # every mid point the number of hours required and consider the min no.

    if h == max(piles):
        return max(piles)
    left, right = 1, max(piles)
    result = right

    while left <= right:
        mid = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)
        if hours <= h:
            result = min(result, mid)
            right = mid - 1
        else:
            left = mid + 1
    return result


print(min_eating_speed([3, 6, 7, 11], 8))  # 4
print(min_eating_speed([30, 11, 23, 4, 20], 5))  # 30
