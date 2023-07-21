# User function Template for python3
'''
    Function to return the value at point of intersection
    in two linked list, connected in y shaped form.

    Function Arguments: head_a, head_b (heads of both the lists)

    Return Type: value in NODE present at the point of intersection
                 or -1 if no common point.

    Contributed By: Nagendra Jha

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''

# User function Template for python3
'''
    Function to return the value at point of intersection
    in two linked list, connected in y shaped form.

    Function Arguments: head_a, head_b (heads of both the lists)

    Return Type: value in NODE present at the point of intersection
                 or -1 if no common point.

    Contributed By: Nagendra Jha

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''


# Function to find intersection point in Y shaped Linked Lists.
def interestPoint(headA, headB):
    c1 = 0
    tempA = headA
    while tempA:
        c1 += 1
        tempA = tempA.next

    c2 = 0
    tempB = headB
    while tempB:
        c2 += 1
        tempB = tempB.next

    if c1 > c2:
        diff = c1 - c2
        for i in range(0, diff):
            headA = headA.next
    elif c2 > c1:
        diff = c2 - c1
        for i in range(0, diff):
            headB = headB.next

    while headA and headB:
        if headA == headB:
            return headA.data

        headA = headA.next
        headB = headB.next

    return -1




