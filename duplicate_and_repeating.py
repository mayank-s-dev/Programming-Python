def findTwoElement(arr, n):
    # code here
    # solution 1

    arr.sort()
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i

    print(total_sum)
    curr_sum = 0
    for i in range(0, n):
        curr_sum += arr[i]

    print(curr_sum)
    for i in range(0, n - 1):
        if arr[i] == arr[i + 1]:
            print(total_sum - curr_sum + arr[i])
            return [arr[i], total_sum - curr_sum + arr[i]]

def findTwoElement2(arr, n):
    # code here
    missing = 0
    for i in range(0, n):
        index = abs(arr[i]) - 1

        if arr[index] < 0:
            repeating = abs(arr[i])
        else:
            arr[index] *= -1

    missing = 0
    print(arr, repeating)
    for i in range(0, n):
        if arr[i] > 0:
            missing = i + 1

    return [repeating, missing]

a = findTwoElement2([2, 4, 1, 2, 5], 5)
print(a)