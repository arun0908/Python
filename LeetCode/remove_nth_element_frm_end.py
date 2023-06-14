"""
Given the head of a linked list, remove the nth node from the end of the list
and return its head.
"""


from typing import Optional


class ListNode:
    """
    Class denoting the logic for a linked list
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_fromend(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove the nth element from the end of a list node
    """
    # # Creating an dummy node to initialse first pointer
    # dummy = ListNode(0, head)

    # # Initilise first and second pointer
    # first = dummy
    # second = head

    # # Moving the second pointer after n positions
    # while n > 0 and second:
    #     second = second.next
    #     n -= 1

    # # Move pointers till the second pointer is not null and reaches the end
    # while second:
    #     first = first.next
    #     second = second.next

    # # Deleting the nth index element
    # first.next = first.next.next

    # return dummy.next

    length = 0
    if head is None:
        return head
    if head.next is None:
        return None
    node = head
    while node:
        length += 1
        node = node.next
    if length == n:
        return head.next
    node = head
    diff = length - n
    for i in range(1, diff):
        node = node.next
    node.next = node.next.next
    return head


print(remove_nth_fromend([1, 2, 3, 4, 5], 2))  # [1,2,3,5]
print(remove_nth_fromend([1], 1))  # []
