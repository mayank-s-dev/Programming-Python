# User function Template for python3
'''
    Your task is to segregate the list of
    0s,1s and 2s.

    Function Arguments: head of the original list.
    Return Type: head of the new list formed.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }

'''


class Solution:
    # Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        count_one = 0
        count_two = 0
        count_zero = 0

        curr = head
        while curr:
            if curr.data == 0:
                count_zero += 1
            elif curr.data == 1:
                count_one += 1
            else:
                count_two += 1

            curr = curr.next

        curr = head
        while curr:
            if count_zero > 0:
                curr.data = 0
                count_zero -= 1
            elif count_one > 0:
                curr.data = 1
                count_one -= 1
            else:
                curr.data = 2

            curr = curr.next

        return head

        # code here
        """
        count_one = 0
        count_two = 0
        count_zero = 0

        curr = head
        while curr:
            if curr.data == 0:
                count_zero += 1
            elif curr.data == 1:
                count_one += 1
            else:
                count_two += 1

            curr = curr.next

        head = None
        curr = None
        while count_zero:
            new_node = Node(0)
            if head is None:
                head = new_node
            else:
                curr.next = new_node

            curr = new_node
            count_zero -= 1

        while count_one:
            new_node = Node(1)
            if head is None:
                head = new_node
            else:
                curr.next = new_node

            curr = new_node
            count_one -= 1

        while count_two:
            new_node = Node(2)
            if head is None:
                head = new_node
            else:
                curr.next = new_node

            curr = new_node
            count_two -= 1

        return head
        """
