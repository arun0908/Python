#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any
# order.
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Solution: The basic solution would be to map the elements in the array to their count of occurrences, sort the map in
#           descending order, based on their value and append the result to an array till the required count is achieved.
# A more optimised solution in O(n) time would be to construct the map and their values, but use bucket sort along with
# it. After creating a dictionary, we can consider an array with count as indexes and the elements in the array with those
# counts as values. The length of array would be the same as the input array, because the worst case is all the elements
# in the input occur only once. Then we can map the count from the map to the array based on key,value and then append
# the elements from the highest count in reverse to a resultant array till the length of the array is = to k

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count_map = {}
    for n in nums:
        count_map[n] = 1 + count_map.get(n, 0)
    # count_map = dict(sorted(count_map.items(), key=lambda x: x[1], reverse=True))
    # result = []
    # for i in count_map:
    #     if k>0:
    #         result.append(i)
    #         k -= 1
    # return result
    sort_arr = [[] for i in range(len(nums) + 1)]
    for value, count in count_map.items():
        sort_arr[count].append(value)
    result = []
    for i in range(len(sort_arr) - 1, 0, -1):
        for j in sort_arr[i]:
            result.append(j)
            if len(result) == k:
                return result


print(topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
print(topKFrequent([1],1))  # [1]

