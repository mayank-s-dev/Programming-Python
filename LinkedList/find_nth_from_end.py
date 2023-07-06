def getNthFromLast(head, N):
    # code here
    # checked submission, very nice approach using two variables/pointers
    if head is None:
        return -1

    first = head
    second = head

    while N:
        if first == None:
            return -1

        N -= 1
        first = first.next

    while first:
        second = second.next
        first = first.next

    return second.data

    """
    # self approach
    if head is None:
        return -1

    curr = head
    total = 0

    while curr:
        total += 1
        curr = curr.next

    if N > total:
        return -1

    # kth node from start
    kth = total - N + 1
    curr = head
    prev = head

    if kth == 1:
        return head.data

    while curr:
        if kth == 1:
            return curr.data
        else:
            kth -= 1
            curr = curr.next

    """