"""
Given the head of a singly linked list, reverse the list, and return the
reversed list.
"""


from typing import Optional


class ListNode:
    """
    Class denoting the logic for a linked list
    """

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Method to reverse a linked list
    """
    current = head
    previous = None

    while current:
        next_node = current.next_node
        current.next_node = previous
        previous = current
        current = next_node

    return previous


print(reverse_list([1, 2, 3, 4, 5]))  # [5,4,3,2,1]
print(reverse_list([1, 2]))  # [2,1]
