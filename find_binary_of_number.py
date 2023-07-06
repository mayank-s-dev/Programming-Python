def bin(n):
    if (n > 1):
        bin(n >> 1)
    print(n & 1, end="")


# Driver code
# bin(131)
print()
bin(3)


"""
# solution 1
def binary(n, res):
    if n == 1:
        res.append(1)
        return res.reverse()

    d = n % 2
    print(n, d)
    res.append(d)

    n = n // 2
    binary(n, res)

    return res

print(binary(7, []))
"""
