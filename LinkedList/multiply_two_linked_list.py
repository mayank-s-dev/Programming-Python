def multiplyTwoList(head1, head2):
    # Code here
    num1 = 0
    num2 = 0

    MOD = 10 ** 9 + 7

    while head1 or head2:
        if head1:
            num1 = (num1 * 10 + head1.data) % MOD
            head1 = head1.next

        if head2:
            num2 = (num2 * 10 + head2.data) % MOD
            head2 = head2.next

    return (num1 * num2) % MOD
