class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head Node created:", self.head.value)
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Appended new Node with value:", self.tail.value)


dllist = DoublyLinkedList()
dllist.append("First Node")
print(dllist.head.value)
print(dllist.tail.value)
dllist.append("Second Node")
print(dllist.head.value)
print(dllist.tail.value)
print(dllist.head.next.value)
print(dllist.tail.prev.value )
print(dllist.head.prev.value)
print(dllist.tail.next.value)
print(dllist.append("Third Node"))
print(dllist.tail.value)
print(dllist.tail.prev.value)
print(dllist.tail.prev.prev.value)
print(dllist.head.next.next.value)