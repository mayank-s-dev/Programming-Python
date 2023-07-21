'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''


class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        slow = head
        fast = head
        flag = False

        while slow and fast and slow.next and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                flag = True
                break

        slow = head
        prev = fast
        if flag and fast == head:
            prev = head.next

            while prev.next != head:
                prev = prev.next

            prev.next = None
            return

        if flag:
            while slow != fast:
                prev = fast
                slow = slow.next
                fast = fast.next

            prev.next = None
            return