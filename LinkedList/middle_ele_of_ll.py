# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''


class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1

    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        ## one approach be using slow and fast pointer
        curr = head
        total_count = 0
        while curr:
            total_count += 1
            curr = curr.next

        position = int(total_count / 2) + 1
        curr = head
        while curr:
            if position == 1:
                return curr.data

            position -= 1
            curr = curr.next


