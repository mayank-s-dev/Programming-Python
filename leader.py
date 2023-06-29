def leaders(A, N):
    # Code here
    sum = 0
    leader = []
    for i in range(N - 1, -1, -1):
        print(i, A[i])
        if A[i] > sum:
            leader.append(A[i])
            sum += A[i]

    return leader

res = leaders([30, 66, 78, 74, 91, 76, 60, 20, 13, 67], 10)
print(res)