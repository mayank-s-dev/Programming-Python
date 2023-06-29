def find3number(A, n):
    # code here
    min_index_arr = [0] * n
    min_index_arr[0] = -1
    small = 0

    max_index_array = [0] * n
    max_index_array[n - 1] = -1
    largest = n - 1

    for i in range(1, n):
        if A[i] <= A[small]:
            min_index_arr[i] = -1
            small = i
        else:
            min_index_arr[i] = small

    print(min_index_arr)
    for i in range(n - 2, -1, -1):
        if A[i] <= A[largest]:
            max_index_array[i] = largest
        else:
            max_index_array[i] = -1
            largest = i
    print(max_index_array)
    for i in range(1, n - 1):
        if min_index_arr[i] != -1 and max_index_array != -1:
            return [A[min_index_arr[i]], A[i], A[max_index_array[i]]]

    return []

lis = find3number([1, 2 ,1, 1, 3], 5)
print(lis)


