# User function Template for python3

'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''


class Solution:

    # Function to count nodes of a linked list.
    def getCount(self, head_node):
        # code here
        if head_node is None:
            return 0

        curr = head_node
        count = 0
        while curr:
            count += 1
            curr = curr.next

        return count
