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

    def delete_nth_node_from_last(self, N):
        if self.head is None:
            return

        curr = self.head
        total = 0

        while curr is not None:
            total += 1
            curr = curr.next

        if N > total:
            return

        # kth node from start
        kth = total - N + 1
        curr = self.head
        prev = self.head

        """
        # without outer prev
        if kth == 1:
            prev = self.head.next
            self.head.next = None
            self.head = prev
            return

        while curr is not None:
            if kth == 2:
                prev = curr.next.next
                curr.next.next = None
                curr.next = prev
                break
            else:
                kth -= 1
                prev = curr
                curr = curr.next
        """
        if kth == 1:
            prev = self.head.next
            self.head.next = None
            self.head = prev
            return

        while curr is not None:
            if kth == 1:
                prev.next = curr.next
                curr.next = None
                break
            else:
                kth -= 1
                prev = curr
                curr = curr.next


# Create a linked list object
llist = LinkedList()

# Add new nodes to the linked list
llist.push(500)
llist.push(30)
llist.push(11)
llist.push(21)
llist.push(14)

llist.delete_nth_node_from_last(5)
temp = llist.head
while temp:
    print(temp.data)
    temp = temp.next
