"""Add a couple methods to our LinkedList class, and use that to implement a Stack.
You have 4 functions below to fill in: insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first" function than just use "append"?"""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

        current = self.head
        current_pos = 1
        if not self.head:
            return None
        while current:
            if current_pos == position:
                return current
            current = current.next
            current_pos += 1
        if not current.next:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        current = self.head
        current_pos = 1
        if not self.head:
            return None
        while current:
            if current_pos == position - 1:
                new_element.next = current.next
                current.next = new_element
            current = current.next
            current_pos += 1

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        if current.value == value:
            self.head = current.next
            return
        while current:
            if value == current.value:
                previous.next = current.next
                break
            previous = current
            current = current.next

    def insert_first(self, new_element):
        """Insert new element as the head of the LinkedList"""
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        """Delete the first (head) element in the LinkedList as return it"""
        current = self.head
        self.head = self.head.next
        return current


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        """Push (add) a new element onto the top of the stack"""
        self.ll.insert_first(new_element)

    def pop(self):
        """Pop (remove) the first element off the top of the stack and return it"""
        return self.ll.delete_first()


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
"""print(stack.pop())"""
stack.push(e4)
print(stack.pop().value)