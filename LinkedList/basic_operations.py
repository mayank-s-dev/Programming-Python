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

    def find(self, key):
        if self.check_head():
            return

        curr = self.head

        while curr is not None:
            if curr.data == key:
                return True

            curr = curr.next

        return False

    def insert_at_end(self, key):
        curr = self.head
        new_node = Node(key)
        if curr is None:
            self.head = new_node
            return

        while curr.next:
            curr = curr.next

        curr.next = new_node

    def insert_after_key(self, key, new_key):
        if self.check_head():
            return

        new_node = Node(new_key)
        curr = self.head
        while curr:
            if curr.data == key:
                new_node.next = curr.next
                curr.next = new_node
                break
            else:
                curr = curr.next

    def delete_from_beginning(self):
        if self.check_head():
            return

        self.head = self.head.next

    def delete_specific_key(self, key):
        if self.check_head():
            return

        curr = self.head
        prev = self.head
        while curr:
            if curr.data == key:
                prev.next = curr.next
                curr.next = None
                break
            else:
                prev = curr
                curr = curr.next

    def delete_from_end(self):
        if self.check_head():
            return

        curr = self.head
        prev = self.head
        while curr.next is not None:
            prev = curr
            curr = curr.next

        prev.next = None

    

# Create a linked list object
llist = LinkedList()

# Add new nodes to the linked list
llist.push(500)
llist.push(30)
llist.push(11)
llist.push(21)
llist.push(14)

# print(llist.find(500))
llist.insert_at_end(90)
llist.insert_after_key(21, 22)
llist.delete_from_beginning()
llist.delete_from_end()
llist.delete_from_end()
llist.delete_specific_key(500)
temp = llist.head
while temp:
    print(temp.data)
    temp = temp.next
