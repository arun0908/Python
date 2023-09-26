"""
A tree data structure is similar to a linked list, where in a linked list,
every node holds a data and the next pointer to the next node.
In a linked list every node is connected to just one other node. Whereas in a
tree data structure there are more than one pointers to other node,
i.e every node holds some data and the pointer to one or more nodes.

Technically every linked list is a tree. If any node in the tree contains more
than one reference or pointer to itself, then that is not
called a tree. If a tree holds the pointer information to 2 nodes, then it is
called a binary tree. For a better understanding trees are represented in a
top down manner, so in a binary tree there are two nodes, namely left and
right.
"""


def find_sum(root):
    """
    Given the root node of a binary tree with right and left nodes,
    find the sum of all elements in a tree.
    Follow-up: Solve in O(n) time
    """
    if root is None:
        return 0
    if root.left or root.right:
        return root.data + find_sum(root.left) + find_sum(root.right)
    return root.data
