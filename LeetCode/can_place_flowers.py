# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted
# in adjacent plots. Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
# and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers
# rule.

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    temp = [0] + flowerbed + [0]
    for i in range(1, len(temp)-1):
        if temp[i-1] == 0 and temp[i] == 0 and temp[i+1] == 0:
            n -= 1
            temp[i] = 1
    return n <= 0


print(canPlaceFlowers([1, 0, 0, 0, 1], 1))  # True
print(canPlaceFlowers([1, 0, 0, 0, 1], 2))  # False
