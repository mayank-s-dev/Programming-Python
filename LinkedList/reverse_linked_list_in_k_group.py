"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  This is method only submission.
  You only need to complete the method.
"""


class Solution:
    def reverse(self, head, k):
        # Code here
        # solved on leetcode
        # https://leetcode.com/problems/reverse-nodes-in-k-group/

        if head is None:
            return head

        count = 0
        curr = head

        # while curr:
        #     count += 1
        #     curr = curr.next

        # if count < k:
        #     return head

        curr = head
        prev = None
        start = head
        count = 0
        while curr:
            count += 1
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

            if count == k:
                start.next = self.reverse(curr, k)
                return prev

        start.next = self.reverse(curr, k)
        return prev