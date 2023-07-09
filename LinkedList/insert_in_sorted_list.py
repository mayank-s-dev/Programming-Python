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

    def sortedInsert(self, key):
        # code here
        head1 = self.head
        # return head of edited linked list
        new_node = Node(key)
        if head1 is None:
            head1 = new_node
            return head1

        appended = False
        if head1.data > key:
            new_node.next = head1
            head1 = new_node
            appended = True

        temp = head1
        prev = head1

        while temp and not appended:
            val = temp.data
            if val < key:
                prev = temp
                temp = temp.next
            else:
                prev.next = new_node
                new_node.next = temp
                appended = True
                break

        if not appended:
            prev.next = new_node

        return head1


# Create a linked list object
llist = LinkedList()

# Add new nodes to the linked list
llist.push(7)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(-1)

# llist.skipMdeleteN(2, 1)
temp = llist.sortedInsert(-10)
# temp = llist.head
# print("S", temp.data)
while temp:
    print(temp.data)
    temp = temp.next
