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

    def divide(self):
        # code here
        head = self.head
        itr = head
        odd = None
        even = None
        odd_start = None
        even_start = None

        while itr:
            # print("a", itr.data)
            if itr.data % 2 == 0:
                if even is None:
                    even = itr
                    even_start = even
                else:
                    even.next = itr
                    even = itr
            else:
                if odd is None:
                    odd = itr
                    odd_start = odd
                else:
                    odd.next = itr
                    odd = itr

            itr = itr.next

        print("fffffff", even_start.data, odd_start.data)

        even.next = odd_start
        odd.next = None
        # head = even_start
        return even_start

# Create a linked list object
llist = LinkedList()

# Add new nodes to the linked list
llist.push(7)
llist.push(5)
# llist.push(4)
llist.push(3)
# llist.push(2)
llist.push(1)

temp = llist.divide()
# temp = llist.head
# print("S", temp.data)
while temp:
    print(temp.data)
    temp = temp.next
