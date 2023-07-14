# not working with my code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # push new value to linked list
    # using append method
    def append(self, new_value):

        # Allocate new node
        new_node = Node(new_value)

        # if head is None, initialize it to new node
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        # Append the new node at the end
        # of the linked list
        curr_node.next = new_node

    def mergemine(self, head1, head2):
        temp = None
        new_head = None
        if head1 == None and head2 == None:
            return None
        if head1 == None:
            return head2
        if head2 == None:
            return head1

        while head1 and head2:
            if head1.data <= head2.data:
                if new_head is None:
                    new_head = head1
                    temp = head1
                    temp = temp.next
                else:
                    temp.next = head1
                    head1 = head1.next
                    temp = temp.next
            else:
                if new_head is None:
                    new_head = head2
                    temp = head2
                    temp = temp.next
                else:
                    temp.next = head2
                    head2 = head2.next
                    temp = temp.next

        while head1 is not None:
            print(temp.data)
            temp.next = head1

        while head2 is not None:
            print(temp.data)

            temp.next = head2

        return new_head

    def merge(self, a, b):
        if a == None and b == None:
            return None
        if a == None:
            return b
        if b == None:
            return a
        if a.data <= b.data:
            head = a
            tail = a
            a = a.next
        else:
            head = b
            tail = b
            b = b.next
        while a != None and b != None:
            if a.data <= b.data:
                tail.next = a
                a = a.next
                tail = tail.next
            else:
                tail.next = b
                b = b.next
                tail = tail.next
        if a != None:
            tail.next = a
        if b != None:
            tail.next = b
        return head

    def mergeSort(self, head):
        if head is None or head.next is None:
            return head

        # mid=mid_point_2(head)
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        head2 = self.mergeSort(mid.next)
        mid.next = None
        head1 = self.mergeSort(head)
        # print(head1.data, head2.data)
        final_head = self.mergemine(head1, head2)
        return final_head


# Utility function to print the linked list
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')


# Driver Code
if __name__ == '__main__':
    li = LinkedList()

    # Let us create a unsorted linked list
    # to test the functions created.
    # The list shall be a: 2->3->20->5->10->15
    li.append(15)
    li.append(10)
    li.append(5)
    li.append(20)
    li.append(3)
    li.append(2)

    # Apply merge Sort
    li.head = li.mergeSort(li.head)
    print("Sorted Linked List is:")
    printList(li.head)
