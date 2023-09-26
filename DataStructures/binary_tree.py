"""
Python module to define a binary tree and the insertion and finding of
an element in a binary tree
"""


class Node:
    """
    Node class
    """

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value) -> None:
        """
        Insert data in a binary node
        """
        if value <= self.data:
            if self.left:
                self.left.insert(value)
            self.left = Node(value)
        else:
            if self.right:
                self.right.insert(value)
            self.right = Node(value)

    def contains(self, value) -> bool:
        """
        Find a value as part of the tree
        """
        if self.data == value:
            return True
        elif value < self.data:
            if self.left:
                return self.left.contains(value)
            return False
        elif value > self.data:
            if self.right:
                return self.right.contains(value)
            return False

    def inorder_traversal(self) -> None:
        """
        Print inorder traversal for a binary tree
        """
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self) -> None:
        """
        Print preorder traversal for a binary tree
        """
        print(self.data)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self) -> None:
        """
        Print postorder traversal for a binary tree
        """
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.data)
