# Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
# (i) a next pointer to the next node,
# (ii) a bottom pointer to a linked list where this node is head.
# Each of the sub-linked-list is in sorted order.
# Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order.

# User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

'''


def merge(curr1, curr2):
    if curr1 is None:
        return curr2

    if curr2 is None:
        return curr1

    result = None
    if curr1.data < curr2.data:
        result = curr1
        result.bottom = merge(curr1.bottom, curr2)
    else:
        result = curr2
        result.bottom = merge(curr1, curr2.bottom)

    result.next = None
    return result


def flatten(root):
    # Your code here
    if root is None or root.next is None:
        return root

    root.next = flatten(root.next)
    root = merge(root, root.next)
    return root

    """
    # solved using merged sort
    curr1 = root
    while curr1 and curr1.next:
        curr2 = curr1.next
        curr1.next = curr2.next
        junc = curr1
        prev = curr1

        while curr1 and curr2:
            if curr1.data < curr2.data:
                prev = curr1
                curr1 = curr1.bottom
            elif curr1.data > curr2.data:
                prev.bottom = curr2
                prev = curr2
                temp = curr2.bottom
                curr2.bottom = curr1
                curr2 = temp


        while curr2:
            prev.bottom = curr2
            prev = curr2
            curr2 = curr2.bottom

        curr1 = junc

    return root
    """




