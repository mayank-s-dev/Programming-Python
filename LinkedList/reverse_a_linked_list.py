class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def check_head(self):
        if self.head is None:
            return True

    def push(self, new_key):
        new_node = Node(new_key)
        new_node.next = self.head
        self.head = new_node

    def reverse_linked_list(self):
        prev = self.head
        curr = prev.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        self.head.next = None
        head = prev
        return head


# Create a linked list object
llist = LinkedList()

# Add new nodes to the linked list
llist.push(0)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

temp = llist.reverse_linked_list()
while temp:
    print(temp.data)
    temp = temp.next
