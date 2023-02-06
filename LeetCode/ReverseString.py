# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.


def reverseString(s: list[str]) -> None:
    # Using a two pointer approach which is efficient and does the assignment in-place
    l, r = 0, len(s)-1
    while l < r:
        # temp = s[l]
        # s[l] = s[r]
        # s[r] = temp

        # Tuple assignment in python eliminates the need to use a temporary variable
        # In a tuple assignment the lhs is consideres as tuple variables and rhs as tuple values.
        # Assigning values takes place simultaneously, so in this case rhs already loads the values and assignings them simultaneously
        # so if s[l] , s[r] were initially 1 and 2, at assignment it is done as (s[l] , s[r]) = (2 , 1) and 2 is set to l, 1 to r
        s[l], s[r] = s[r], s[l]
        l, r = l + 1, r - 1

    # Using a stack approach, but it uses O(n) extra space
    # temp_stack = []
    # for c in s:
    #     temp_stack.append(c)

    # After populating stack, we can use LIFO (last in first out of a stack) to populate original string
    # i = 0
    # while temp_stack:
    #     s[i] = temp_stack.pop()
    # For de-bugging purposes
    print(s)

    # We can use recurssion to solve, by reversiong from out to in, by calling in the function again and again, but reduces speed times

    # Define a function to call recurssively
    # def recurrsive(l , r):
    #     if l < r:
    #         s[l] , s[r] = s[r] , s[l]
    #         recurrsive(l + 1, r - 1)
    # recurrsive(l , r)  # l , r defined in the first step


print(reverseString(["h", "e", "l", "l", "o"]))  # ['o', 'l', 'l', 'e', 'h']
