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

    def loop_length(self):
        # floyd cycle finding algorithm
        if self.head is None:
            return 0

        count = 0
        slow = self.head
        fast = self.head
        start_flag = 0
        while slow and fast and slow.next and fast.next.next:
            if slow == fast and not start_flag:
                count = 1
                slow = slow.next
                while slow != fast:
                    slow = slow.next
                    count += 1

                break

            slow = slow.next
            fast = fast.next.next
            start_flag = 1

        return count

        """
        # my approach 
        dict = {}
        if self.head is None:
            return True

        curr = self.head
        curr_length = 0
        while curr is not None:
            curr_length += 1
            n = dict.get(curr)
            if n:
                return curr_length - n

            dict[curr] = curr_length
            curr = curr.next

        return 0
        """


# Create a linked list object
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

print(llist.loop_length())
