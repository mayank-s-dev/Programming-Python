def mergeTwoLists(self, list1, list2):
    # recursive approach
    if list1 is None:
        return list2

    if list2 is None:
        return list1

    if list1.val <= list2.val:
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
    """
    # iterative approach
    if not list1:
        return list2

    if not list2:
        return list1

    curr1 = list1
    curr2 = list2

    if curr2.val < curr1.val:
        curr2, curr1 = curr1, curr2

    res = curr1
    prev = curr1
    while curr1 and curr2:
        if curr1.val <= curr2.val:
            prev = curr1
            curr1 = curr1.next
        else:
            prev.next = curr2
            prev = curr2
            temp = curr2.next
            curr2.next = curr1
            curr2 = temp

    if curr1:
        prev.next = curr1

    if curr2:
        prev.next = curr2

    return res
    """