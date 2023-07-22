class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def findIntersection(self, head1, head2):
        # code here
        # return head of intersection list
        if head1 is None:
            return None

        if head2 is None:
            return None

        dict = {}
        while head2:
            if dict.get(head2) is None:
                dict[head2.data] = True

            head2 = head2.next

        new_head = None
        curr = None
        while head1:
            if dict.get(head1.data):
                if new_head is None:
                    curr = head1
                    new_head = curr
                else:
                    temp = Node(head1.data)
                    curr.next = temp
                    curr = curr.next

            head1 = head1.next

        curr.next = None
        return new_head
