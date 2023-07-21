# class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
def isCircular(head):
    # Code here
    start = head
    if head is None:
        return True

    head = head.next
    while head is not None and head is not start:
        head = head.next

    return start == head

