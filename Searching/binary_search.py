def binarySearch(input_arr, n, x):
    # code here
    left = 0
    right = n - 1

    while left < right:
        mid = (left + right)//2
        if input_arr[mid] > x:
            right = mid - 1
        elif input_arr[mid] < x:
            left = mid + 1
        else:
            return mid

        # print(mid)
    return -1


def recursive_binary_search(input_arr, x, left, right):
    if left > right:
        return -1

    mid = left + (right - 1) // 2
    if input_arr[mid] == x:
        return mid
    elif input_arr[mid] > x:
        right = mid - 1
        return recursive_binary_search(input_arr, x, left, right)
    else:
        left = mid + 1
        return recursive_binary_search(input_arr, x, left, right)


# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    x = 1

    # Function call
    result = binarySearch(arr, 5, x)
    # result = recursive_binary_search(arr, x, 0, len(arr))

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
