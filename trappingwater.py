def trappingWater(arr, n):
    # Code here

    l_max = [-1] * n
    max = arr[0]
    for i in range(1, n):
        l_max[i] = max
        if arr[i] > max:
            max = arr[i]

    max = arr[n - 1]
    print("Sss", max)
    r_max = [-1] * n
    for i in range(n - 2, -1, -1):
        r_max[i] = max
        if arr[i] > max:
            max = arr[i]

    total = 0
    for i in range(1, n - 1):
        curr = min(l_max[i], r_max[i]) - arr[i]
        if curr > 0:
            total += curr

    print(l_max)
    print(r_max)
    print(total)
    return total

trappingWater([8, 8, 2, 4, 5, 5, 1], 7)