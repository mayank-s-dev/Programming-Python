# User function Template for python3

'''
# Linked List Node
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        '''


#
# Given a singly linked list, the task is to rearrange it in a way that all odd position nodes are together and all
# even positions node are together. Assume the first element to be at position 1 followed by second element at
# position 2 and so on. Note: You should place all odd positioned nodes first and then the even positioned ones. (
# considering 1 based indexing). Also, the relative order of odd positioned nodes and even positioned nodes should be
# maintained
def rearrangeEvenOdd(head):
    # code here
    odd = head
    even = head
    if head:
        even = odd.next

    even_start = even
    while odd and even:
        if even.next is None:
            odd.next = even_start
            break
        else:
            odd.next = even.next
            odd = even.next

        if odd.next is None:
            even.next = None  # odd.next
        else:
            even.next = odd.next
            even = odd.next


class Solution:
    pass
