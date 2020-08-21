"""
Include LinkedList, LinkedListNode,
SinglyLinkedList, SinglyLinkedListNode,
DoublyLinkedList, DoublyLinkedListNode,
CircularSinglyLinkedList, CircularSinglyLinkedListNode,
CircularDoublyLinkedList, CircularDoublyLinkedListNode"""


class SinglyLinkedListNode(object):
    """docstring for SinglyLinkedListNode"""

    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__str__()})'

    def __copy__(self):
        return SinglyLinkedListNode(self.val, self.next_)

    def copy(self):
        return self.__copy__()


class SinglyLinkedList(object):
    """docstring for SinglyLinkedList"""

    def __init__(self, head=None):
        self.head = head
        self.size = 1 if self.head else 0

    def _enable_direct_data_pass(f):
        """Convert to SLLNode if other data types are passed"""

        def wrapper(self, node, *args, **kwargs):
            if not isinstance(node, SinglyLinkedListNode):
                node = SinglyLinkedListNode(val=node)
            f(self, node, *args, **kwargs)
        return wrapper

    def _increment_size(f):
        def wrapper(self, *args, **kwargs):
            f(self, *args, **kwargs)
            self.size += 1
        return wrapper

    def last(self):
        current = self.head
        while current and current.next_:
            current = current.next_
        return current

    def first(self):
        return self.head

    def traverse(self):
        current = self.head
        while current:
            yield current
            current = current.next_

    def _insert(self, node, location):
        if location < -1 or location > self.size:
            raise IndexError
        if self.size:
            if location == -1:
                located = self.last()
            elif location == 0:
                return self._prepend(node)
            else:
                traversal = self.traverse()
                while location:
                    located = next(traversal)
                    location -= 1
            located.next_, node.next_ = node, located.next_
        else:
            self.head = node

    def _prepend(self, node):
        node.next_, self.head = self.head, node

    @_enable_direct_data_pass
    @_increment_size
    def prepend(self, node):
        self._prepend(node)

    @_enable_direct_data_pass
    @_increment_size
    def append(self, node):
        self._insert(node, -1)

    @_enable_direct_data_pass
    @_increment_size
    def insert(self, node, location):
        self._insert(node, location)

    def remove(self, val):
        for node in self.traverse():
            if node.next_.val == val:
                node.next_ = node.next_.next_
                break
        else:
            raise ValueError

    def clear(self):
        self.head = None
        self.size = 0

    def copy(self):
        return self.__copy__()

    def count(self, val):
        traversal = self.traverse()
        counter = 0
        for node in traversal:
            if node.val == val:
                counter += 1
        return counter

    def extend(self, other):
        # must be iterable
        if isinstance(other, SinglyLinkedList):
            return self.append(other.head)
        sll = SinglyLinkedList()
        for obj in other:
            sll.insert(obj)

    def index(self, val):
        for i, node in enumerate(self.traverse()):
            if node.val == val:
                return i
        raise ValueError

    def pop(self, location):
        # rework
        if self.size > location >= 0:
            traversal = self.traverse()
            for i in range(location):
                located = next(traversal)
            result = located.copy()
            located.next_ = next(traversal).next_
            return result
        else:
            raise IndexError

    def reverse(self):
        if self.size > 1:
            head = self.head
            previous = head.copy()
            previous.next_ = None
            head = head.next_
            current = head
            while head:
                head = head.next_
                current.next_ = previous
                previous, current = current, head
            self.head = previous

    def sort(self):
        return NotImplemented

    def __str__(self):
        if not self.size:
            return 'Empty SLL'
        return ' -> '.join(map(str, self.traverse()))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__str__()})'

    def __len__(self):
        return self.size

    def __getitem__(self, location):
        # rework
        if self.size > location >= 0:
            traversal = self.traverse()
            for i in range(location + 1):
                located = next(traversal)
            return located
        else:
            raise IndexError

    def __setitem__(self, location, val):
        self[location].val = val

    def __delitem__(self, location):
        """Removes the nth item from the list"""
        # rework
        if self.size > location >= 0:
            traversal = self.traverse()
            for i in range(location):
                located = next(traversal)
            located.next_ = next(traversal).next_
        else:
            raise IndexError

    def __copy__(self):
        """Shallow copy of SLL"""
        sll = SinglyLinkedList(self.head)
        sll.size = self.size
        return sll
