def duplicates(arr, n):
    # code here
    result = []
    hm = {}
    for i in range(0, n):
        if hm.get(arr[i]) is not None:
            hm[arr[i]] += 1
        else:
            hm[arr[i]] = 1

    for i in hm:
        if hm[i] > 1:
            result.append(i)

    if len(result) == 0:
        return [-1]

    return result


# print(duplicates([2, 3, 1, 2, 3], 5))

def duplicates_1(arr, n):
    # code here
    result = [0] * n

    for i in range(0, n):
        result[arr[i]] += 1

    exist = False
    print("ss", result)

    i = 0
    count = 0
    n = len(result)
    while n > 0:
        if result[i] == 0 or result[i] == 1:
            result.pop(i)
            count += 1
        elif result[i] > 1:
            result[i] = i + count
            exist = True
            i += 1
        n -= 1

    if exist:
        return result

    return [-1]


print(duplicates_1([2, 3, 1, 2, 3], 5))
