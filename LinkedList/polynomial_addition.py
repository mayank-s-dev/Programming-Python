"""
Given two polynomial numbers represented by a linked list. The task is to complete the function addPolynomial() that adds these lists meaning adds the coefficients who have the same variable powers.
Note:  Given polynomials are sorted in decreasing order of power.
"""
'''
 class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr
'''


def addPolynomial(self, poly1, poly2):
    p1 = poly1
    p2 = poly2
    prev = None
    new_head = p1

    while p1 or p2:
        if p1 is None:
            prev.next = p2
            break
        elif p2 is None:
            break
        elif p1.power == p2.power:
            p1.coef += p2.coef
            prev = p1
            p1 = p1.next
            p2 = p2.next
        elif p1.power > p2.power:
            prev = p1
            p1 = p1.next
        elif p1.power < p2.power:
            if prev is not None:
                prev.next = p2
            else:
                new_head = p2

            temp = p2.next
            p2.next = p1
            prev = p2
            p2 = temp

    return new_head

    """
    # Code here
    temp1 = poly1
    temp2 = poly2
    newHead = node(0, 0)
    c = newHead;

    while temp1 or temp2:
        if temp1 is None:
            c.next = temp2
            break
        elif temp2 is None:
            c.next = temp1
            break
        elif temp1.power == temp2.power:
            c.next = node(temp1.coef+temp2.coef, temp1.power)
            temp1 = temp1.next
            temp2 = temp2.next
        elif temp1.power > temp2.power:
            c.next = node(temp1.coef, temp1.power)
            temp1 = temp1.next
        elif temp1.power < temp2.power:
            c.next = node(temp2.coef, temp2.power)
            temp2 = temp2.next

        c = c.next

    newHead = newHead.next
    return newHead
    """
