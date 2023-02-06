# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices: list[int]) -> int:
    # A more optimized solution using the sliding window concept, where we consider 2 pointers and update them based on the logic.
    result = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[l] < prices[r]:
            temp = prices[r] - prices[l]
            result = max(result, temp)
        # the trick here would be to update the left pointer, if we find a value lower than our current value, which would,
        # prevent us from using two loops to keep checking for every possibility.
        else:
            l = r
        r += 1
    return result

    # Brute Force approach, but does not work always because of time complexity.

    # for i in range(len(prices)):
    #     for j in range(i + 1, len(prices)):
    #         if prices[i]>prices[j]:
    #             continue
    #         else:
    #             temp = prices[j] - prices[i]
    #             result = max(result, temp)
    # return result


# print(maxProfit([7,1,5,3,6,4]))  # 5 (buy on day 1, sell on day 4)
# print(maxProfit([7,6,4,3,1]))  # 0
print(maxProfit([7, 3, 5, 4, 1, 6]))  # 5
