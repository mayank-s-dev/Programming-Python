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

    def reverseKGroup(self, head, k: int):
        # Code here
        if head is None or k == 0:
            return head

        stack = []
        curr = head
        count = 0
        new_head = None
        new_curr = None
        while curr:
            stack.append(curr)
            temp = curr.next
            count += 1
            if count == k:
                while len(stack) > 0:
                    n = stack.pop()
                    # print(n.data)
                    if new_head == None:
                        new_curr = n
                        new_head = new_curr
                    else:
                        new_curr.next = n
                        new_curr = new_curr.next

                count = 0

            curr = temp

        while len(stack) > 0:
            n = stack.pop()
            n.next = None
            if new_head == None:
                new_curr = n
                new_head = new_curr
            else:
                new_curr.next = n
                new_curr = new_curr.next
        return new_head
# Create a linked list object
llist = LinkedList()

# Add new nodes to the linked list
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

# print(llist.find(500))
# llist.insert_at_end(90)
# llist.insert_after_key(21, 22)
# llist.delete_from_beginning()
# llist.delete_from_end()
# llist.delete_from_end()
# llist.delete_specific_key(500)
r = llist.reverseKGroup(llist.head, 2)
# temp = llist.head
while r:
    print(r.data)
    r = r.next
