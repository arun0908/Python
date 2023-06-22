"""
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.
"""

from typing import Optional


class ListNode:
    """
    Class defining a list node
    """

    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


def add_two_numbers(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Add two numbers as part of a list
    """
    # First Approach
    # Initializing empty strings to hold values
    num1, num2 = "", ""

    # Populating values in num1 and num2
    while list1:
        num1 += str(list1.val)
        list1 = list1.nxt
    while list2:
        num2 += str(list2.val)
        list2 = list2.nxt

    # Calculate the sum of values and initialize a new List node
    num1, num2 = int(num1[::-1]), int(num2[::-1])
    total = str(num1 + num2)[::-1]
    new = ListNode(int(total[0]))
    copy = new

    # Populating the ListNode with values
    for i in total[1:]:
        copy.nxt = ListNode(int(i))
        copy = copy.nxt
    return new

    # Initializing a new node to save the resulting node
    # new = ListNode()
    # curr = new

    # carry = 0
    # # Looping through both the nodes as one may be present and the other may
    # # not be, and including carry if the digits in the last node has a two
    # # digit sum value
    # while l1 or l2 or carry:
    #     val1 = l1.val if l1 else 0
    #     val2 = l2.val if l2 else 0

    #     # Calculating the sum and the carry
    #     val = val1 + val2 + carry
    #     carry = val//10
    #     val = val%10

    #     curr.next = ListNode(val)
    #     curr = curr.next

    #     # Setting l1 and l2 to next if present else None which is the edge
    #     # case where only one digit is present in both the nodes and sum is
    #     # a two digit number
    #     l1 = l1.next if l1 else None
    #     l2 = l2.next if l2 else None

    # return new.next


# print(add_two_numbers([2, 4, 3], [5, 6, 4]))  # [7,0,8]
