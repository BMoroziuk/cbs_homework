class MyList(object):
    class _ListNode(object):
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration
            value = self._next_node.value
            self._next_node = self._next_node.next
            return value

    def __init__(self, iterable=None):
        self._length = 0
        self._head = None
        self._tail = None
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        node = MyList._ListNode(element)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node
        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')
        node = self._head
        for _ in range(index):
            node = node.next
        return node.value

    def __iter__(self):
        return MyList._Iterator(self)


    # Мои функции
    def dell(self, index=None):
        if index == None:
            self._head = self._tail.next
        else:
            pr = self._head
            for _ in range(index - 1):
                pr = pr.next
            pr.next = pr.next.next

    def dellend(self):
        pr = self._head
        for _ in range(self.__len__() - 1):
            pr = pr.next
        pr.next = None

    def inc(self, index, value):
        pr = self._head
        for _ in range(index - 1):
            pr = pr.next
        nx = pr.next
        new = MyList._ListNode(value, pr, nx)
        pr.next = new


def main():
    my_list = MyList([1, 2, 5])
    print(len(my_list))
    print(my_list)
    print()
    for element in my_list:
        print(element)
    print()
    for element in my_list:
        print(element)
    print()
    print(my_list)
    print()


    #Мои функции
    print("Мои функции")
    my_list.inc(2, 3)
    print(my_list)

    my_list.dellend()
    print(my_list)

    my_list.dell(1)
    print(my_list)

    my_list.dell()
    print(my_list)


if __name__ == '__main__':
    main()
