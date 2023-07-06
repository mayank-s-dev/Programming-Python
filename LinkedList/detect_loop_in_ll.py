class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_key):
        new_node = Node(new_key)
        new_node.next = self.head
        self.head = new_node

    def detect_loop(self):
        dict = {}
        if self.head is None:
            return True

        curr = self.head
        while curr is not None:
            if dict.get(curr):
                return True

            dict[curr] = True
            curr = curr.next

        return False


# Create a linked list object
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

print(llist.detect_loop())
