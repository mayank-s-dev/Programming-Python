def TotalPairs(nums, k):
    dict = {}
    count = 0
    res = []
    for i in nums:
        if dict.get(i) is None:
            dict[i] = 1
        else:
            dict[i] += 1

    for i in nums:
        ele1 = i + k
        ele2 = i - k

        if k != 0:
            if dict.get(i) and dict.get(ele1):
                res.append([i, ele1])
                count += 1

            if dict.get(i) and dict.get(ele2):
                res.append([i, ele2])
                count += 1

            dict[i] = 0
        else:
            if dict.get(ele1) > 1:
                count += 1
                dict[i] = 0
    print(res)
    return count




a = [11, 6,10, 5, 11, 16]
print(TotalPairs(a, 5))
