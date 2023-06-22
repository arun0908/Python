"""
Given head, the head of a linked list, determine if the linked list has a
cycle in it. There is a cycle in a linked list if there is some node in the
list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next
pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""


from typing import Optional


class ListNode:
    """
    Linked list class fr building linked list object
    """

    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect if the given linked list has a cycle in it
    """
    # Initial Approach with O(n) memory approach

    # value_set = {}
    # while head:
    #     if head in value_set:
    #         return True
    #     value_set[head] = head
    #     head = head.next
    # return False

    # Optimized approach using Floyd's cycle finding algorithm

    tortoise, hare = head, head

    # Checking with hare as the hare reaches the end sooner and we also want
    # to make sure there is no null in the end so hare.next
    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            return True
    return False


# print(has_cycle([3, 2, 0, -4]))  # position is 1, output = True
