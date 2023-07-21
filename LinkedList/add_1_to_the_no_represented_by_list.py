# User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''


class Solution:
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

    def addOne(self, head):
        # Returns new head of linked List.
        head = self.reverse(head)
        curr = head
        carry = 1
        prev = None
        while carry:
            curr.data += 1
            if curr.data < 10:
                return self.reverse(head)
            else:
                curr.data = 0

            if curr.next is None:
                break
            else:
                curr = curr.next

        curr.next = Node(1)
        return self.reverse(head)

