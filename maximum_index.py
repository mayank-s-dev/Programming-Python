# brute force appraoch
def maximum_index_diff(a, n):
    max_index = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            if a[j] > a[i]:
                temp_diff = j - i
                if temp_diff > max_index:
                    max_index = temp_diff

    return max_index


# print(maximum_index_diff([34, 8, 10, 3, 2, 80, 30, 33, 1], 9))


def maxIndexDiff(A, N):
    # Your code here
    if N == 1:
        return 0

    min_value = A[0]
    Lmin = []
    for i in range(0, N):
        min_value = min(min_value, A[i])
        Lmin.append(min_value)

    max_value = A[N - 1]
    Rmax = []
    for i in range(N - 1, -1, -1):
        max_value = max(max_value, A[i])
        Rmax.append(max_value)

    Rmax.reverse()
    print(Lmin, len(Lmin))
    print(Rmax, len(Rmax))
    max_diff = -1
    left = 0
    right = 0
    while left < N and right < N:
        # print(left, right)
        if Lmin[left] <= Rmax[right]:
            max_diff = max(max_diff, right - left)
            right += 1
        else:
            left += 1

    return max_diff


print(maxIndexDiff([34, 8, 10, 3, 2, 80, 30, 33, 1], 9))
