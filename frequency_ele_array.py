def frequencyCount(N, arr, P):
    # code here
    dict = {}
    for i in range (0, N):
        ele = arr[i]
        if arr[i] in dict:
            dict[ele] += 1
        else:
            dict[ele] = 1

    res = [0] * N
    for i in dict:
        print(i)
        print(res)
        res[i - 1] = dict[i]

    return res

x = frequencyCount(5, [2, 3, 2, 3, 5],5)
print(x)