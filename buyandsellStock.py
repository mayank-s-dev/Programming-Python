def stockBuySell(A, n):
    # code here
    i = 0
    res = [0] * n
    while i < n - 1:
        if A[i] <= A[i + 1]:
            res[i] = 1
        else:
            res[i] = -1

        i += 1

    print(res)
    result = []
    is_buyed = False
    for i in range(0, n - 1):
        if res[i] == 1 and not is_buyed and i == n - 2:
            result.append([i, i + 1])
        elif res[i] == 1 and not is_buyed:
            buy = i
            is_buyed = True
        elif res[i] == 1 and is_buyed and i == n - 2:
            result.append([buy, i + 1])
            is_buyed = False
        elif res[i] == -1 and is_buyed:
            result.append([buy, i])
            is_buyed = False

        print("@@@@@@")
    print(result)
    return res


stockBuySell(
    [858, 1791, 526, 861, 1592, 1516, 387, 1009, 1525, 821, 351, 1787, 413, 554, 103,
     1016, 734, 1354, 1022, 712, 724, 410, 1185, 479, 916, 854, 378, 1065, 980, 1324,
     329, 779, 1505, 463, 670, 1057, 1755, 207, 520, 1138, 968, 1163, 588, 1242, 144,
     707, 1166, 397, 1584, 1159, 1218, 516, 1612, 423, 1178], 55)
