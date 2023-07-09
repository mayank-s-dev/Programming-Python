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

    def skipMdeleteN(self, M, N):
        # Code here
        head = self.head
        if head is None:
            return

        itr = head
        while itr:
            curr1 = itr
            count = 0

            while curr1:
                if count == M - 1:
                    break

                count += 1
                curr1 = curr1.next

            curr2 = curr1
            count_n = 0
            while curr2:
                if count_n == N:
                    break

                count_n += 1
                curr2 = curr2.next

            if curr2 and curr2.next:
                curr1.next = curr2.next
                itr = curr2.next
            else:
                curr1.next = None
                itr = None

        return head

# Create a linked list object
llist = LinkedList()

# Add new nodes to the linked list
llist.push(7)
llist.push(5)
# llist.push(4)
llist.push(3)
# llist.push(2)
llist.push(1)

# llist.skipMdeleteN(2, 1)
temp = llist.divide()
# temp = llist.head
# print("S", temp.data)
while temp:
    print(temp.data)
    temp = temp.next
