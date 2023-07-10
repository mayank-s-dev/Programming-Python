def isPalindrome(self, head):
    # code here: without extra space
    curr = head
    total_count = 0
    while curr:
        total_count += 1
        curr = curr.next

    mid = total_count // 2 + 1

    curr = head
    count = 0
    left = None
    right = None
    while curr:
        count += 1
        if total_count % 2 != 0 and count == mid:
            right = curr.next
            break

        if total_count % 2 == 0 and count == mid:
            right = curr
            break

        temp = curr.next
        curr.next = left
        left = curr
        curr = temp

    while left and right:
        if left.val != right.val:
            return False

        left = left.next
        right = right.next

    return True

    """
    # solved using extra space
    stack = []
    curr = head
    total_count = 0
    while curr:
        total_count += 1
        curr = curr.next

    mid = total_count // 2 if total_count % 2 == 0 else total_count // 2 + 1

    count = 0
    curr = head
    while curr:
        count += 1
        if total_count % 2 != 0 and count == mid:
            stack.append(curr.data)
            break

        stack.append(curr.data)
        curr = curr.next

        if total_count % 2 == 0 and count == mid:
            break

        # stack.append(curr.data)
        # curr = curr.next

    while curr:
        d = curr.data
        s = stack.pop()
        if d != s:
            return False

        curr = curr.next

    return True
    """
