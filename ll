        # code here
        min_index_arr = [0]*n
        min_index_arr[0] = -1
        small = 0

        max_index_arr = [0]*n
        max_index_arr[n-1] = -1
        largest = n - 1

        for i in range(1, n):
            if A[i] <= A[small]:
                min_index_arr[i] = -1
                small = i
            else:
                min_index_arr[i] = small


        for i in range(n - 2, -1, -1):
            if A[i] < A[largest]:
                max_index_arr[i] = largest
            else:
                max_index_arr[i] = -1
                largest = i


        for i in range(1, n - 1):
            if min_index_arr[i] != -1 and max_index_arr != -1:
                return [min_index_arr[i], A[i], max_index_arr[i]]


        return 0