"""
A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n
brand new nodes, where each new node has its value set to the value of its
corresponding original node. Both the next and random pointer of the new nodes
should point to new nodes in the copied list such that the pointers in the
original list and copied list represent the same list state. None of the
pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where
X.random --> Y, then for the corresponding two nodes x and y in the copied
list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each
node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random
pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
"""


# Definition for a Node.
from typing import Optional


class Node:
    """
    Class to initiate and create a node
    """

    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: "Optional[Node]") -> "Optional[Node]":
    """
    Function to create a copy of a given random list
    """
    # Creating a hash map and mapping value of original node and copy node
    value_map = {}

    # Given an edge case where the next pointer points to Null, we need to
    # update the value.
    value_map[None] = None

    # Looping through the given list and mapping values in hash map and
    # creating copy to store values
    current = head
    while current:
        new = Node(0)
        new.val = current.val
        value_map[current] = new
        current = current.next

    # Looping through current again to update the pointer values
    current = head
    while current:
        new = value_map[current]
        new.next = value_map[current.next]
        new.random = value_map[current.random]
        current = current.next

    # Return the head of copied node by referencing its value from hash map
    return value_map[head]

    # new = Node(0, None, None)
    # dummy = new
    # while head:
    #     dummy.val = head.val
    #     if head.next:
    #         dummy.next = Node(head.next.val, None, None)
    #     else:
    #         dummy.next = None
    #     print(dummy.val)
    #     dummy = dummy.next
    #     head = head.next
    # return head


print(
    copy_random_list([[7, "null"], [13, 0], [11, 4], [10, 2], [1, 0]])
)  # [[7,null],[13,0],[11,4],[10,2],[1,0]]
print(copy_random_list([[1, 1], [2, 1]]))  # [[1,1],[2,1]]
