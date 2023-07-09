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

    def pairWiseSwap(self, head):
        # code here
        if head is None:
            return head

        prev = head
        if prev.next:
            head = prev.next
        else:
            return head

        first = None
        while prev:
            curr = prev.next
            if curr is None:
                return head

            if first:
                first.next = curr
            temp = curr.next
            curr.next = prev
            prev.next = temp
            first = prev
            prev = prev.next

        return head

# Create a linked list object
llist = LinkedList()

# Add new nodes to the linked list
llist.push(7)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

# llist.skipMdeleteN(2, 1)
temp = llist.pairWiseSwap()
# temp = llist.head
# print("S", temp.data)
while temp:
    print(temp.data)
    temp = temp.next
