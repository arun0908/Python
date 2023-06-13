"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may
be changed.
"""

from typing import Optional


class ListNode:
    """
    Class denoting the logic for a linked list
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    """
    Reorder the given list in the format mentioned above
    """
    # Breaking the list into two parts
    first_half_pointer = head
    second_half_pointer = head.next

    # Incrementing the pointers and arriving at mid points
    while second_half_pointer and second_half_pointer.next:
        first_half_pointer = first_half_pointer.next
        second_half_pointer = second_half_pointer.next.next

    second = first_half_pointer.next
    first_half_pointer.next = None

    # Reversing the second half of the list
    previous = None
    while second:
        nxt = second.next
        second.next = previous
        previous = second
        second = nxt

    # Merging the two halfs
    while previous:
        nxt1, nxt2 = head.next, previous.next
        head.next = previous
        previous.next = nxt1
        head, previous = nxt1, nxt2


print(reorder_list(head=[1, 2, 3, 4]))  # [1,4,2,3]
print(reorder_list(head=[1, 2, 3, 4, 5]))  # [1,5,2,4,3]
