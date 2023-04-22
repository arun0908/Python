# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
# integer. The digits are ordered from most significant to the least significant in left-to-right order. The large
# integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

def plusOne(digits: list[int]) -> list[int]:
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    digits.insert(0, 1)
    return digits


print(plusOne([1, 2, 3]))  # [1,2,3]
print(plusOne([4, 3, 2, 1]))  # [4,3,2,2]
print(plusOne([9]))  # [1,0]
