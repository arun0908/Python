# You are given an integer array height of length n. There are n vertical
# lines drawn such that the two endpoints of the ith line are (i, 0) and
# (i, height[i]). Find two lines that together with the x-axis form a
# container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

def maxArea(height: list[int]) -> int:
    # brute force
    # result = 0
    # for i in range(len(height)):
    #     for j in range(i+1, len(height)):
    #         area = (j-i) * min(height[i], height[j])
    #         result = max(area, result)
    # return result

    # optimized solution
    result = 0
    left, r = 0, len(height)-1
    while left < r:
        area = (r-left) * min(height[left], height[r])
        result = max(area, result)
        if height[left] <= height[r]:
            left += 1
        else:
            r -= 1
    return result


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(maxArea([1, 1]))  # 1
