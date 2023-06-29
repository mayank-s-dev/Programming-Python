def rotateArr(arr, D, N):
    # Your code here
    if len(arr) == 1:
        return arr

    D = D % N
    first_p = arr[D + 1:N]
    print(first_p)
    second_p = arr[0:D + 1]
    first_p.extend(second_p)
    return first_p


x = rotateArr([1, 2, 3, 4, 5], 2, 5)
# print(x)


def rArr(arr, d):
    n = len(arr)
    d = d % n
    while d > 0:
        temp = arr[-1]
        for i in range(0, n):
            print(i, arr[i])
            curr = arr[i]
            arr[i] = temp
            temp = curr

        d = d - 1
    return arr

y = rArr([1, 2, 3, 4, 5], 3)
print("y", y)