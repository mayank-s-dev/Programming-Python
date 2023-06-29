# find total count of subsequence where i < j < k and a[i] < a[j] < a[k[

def find3number(A, n):
    # code here
    if n < 3:
        return -1

    total_count = 0
    for j in range(1, n - 1):
        count_i = 0
        count_k = 0

        for i in range(0, j):

            if A[i] < A[j]:
                count_i += 1

        for k in range(j + 1, n):
            if A[k] > A[j]:
                count_k += 1

        total_count += count_i * count_k

    return total_count

print(find3number([1, 2 ,1, 1, 3, 4], 6))
