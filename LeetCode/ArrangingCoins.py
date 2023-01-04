# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

def arrangeCoins(n: int) -> int:
     # Brute Force Approach:
        # if n == 1:
        #     return n
        # m = n
        # for i in range(1, m):
        #     n -= i
        #     if n > i:
        #         continue
        #     else:
        #         return i
    
     # Binary search approach, where the time complexity is reduced to O(n). Te trick here is Gauss's formula, which show us how to calculate
     # the sum of n integers from 1 to n, by using (n/2 * (n+1)). In our case we can use binary search to implement, where n will be our rows.

        l , r = 1, n
        # We will consider a res variable to store result, because when we spli the array, if we arrive at a value which say like 1 in case of 5
        # after binary search, we know after using one coin for first row we have more coins, so we store this and continue our binary search
        # where find the max of the result and any value we find.
        res = 0
        while l <= r:
            mid = (l+r)//2
            # As from 1 to n we consider them as rows, we find the coins for a row using the Gauss formula. If the count is more than given coins
            # then that means we need not consider the right part of the no in the range and check on the left side,i.e., less rows
            count = (mid/2)*(mid+1)
            if count > n:
                r = mid -1
            # If the count of coins is less than given, then we can have that as a possibility and we keep searching again from there and not 
            # consider the left side of the possible value, and repeat this till we have no mid value and we return the result.
            else:
                l = mid + 1
                res = max(res,mid)
        return res


print(arrangeCoins(5))  # 2
print(arrangeCoins(8))  # 3