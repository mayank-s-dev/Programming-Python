def majorityElement(A, N):
    # Your code here
    if N == 1:
        return A[0]

    majority_count = int(N / 2)
    print(majority_count)
    A.sort()
    print(A)
    count = 1
    for i in range(1, N):
        if A[i] == A[i - 1]:
            count += 1
        else:
            count = 1

        print(count)
        if count > majority_count:
            print(count, majority_count)
            return A[i]

    return -1


print(majorityElement([2, 2, 1, 1, 1, 1, 1, 1, 1, 2,2, 2, 2, 1, 1 ,2 ,2, 1, 2, 1, 1, 2, 2, 1, 2 ,1 ,2 ,2 ,2 ,1 ,2 ,2 ,1 ,2 ,1 ,1 ,2 ,2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1], 58))
