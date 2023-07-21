# User function Template for python3
'''
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None

'''


class Solution:
    # Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list

        curr = head
        if curr is None:
            return head

        dict = {}
        prev = curr
        while curr:
            if dict.get(curr.data) is None:
                dict[curr.data] = True
                prev = curr
            else:
                prev.next = curr.next

            curr = curr.next

        return head

