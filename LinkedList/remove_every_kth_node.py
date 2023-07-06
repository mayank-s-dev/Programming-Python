# solved on my own
def deleteK(head, k):
    # code here
    if k == 0:
        return head

    if k == 1:
        head = None
        return head

    count = 0
    prev = head
    curr = head

    while curr:
        count += 1
        if count % k == 0:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    return head
