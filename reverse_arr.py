def reverseArr(a, start, end):
    times = int((end - start + 1) / 2)
    i = 0
    while times > 0:
        print("element", a[start + i], a[end - i])
        a[start + i], a[end - i] = a[end - i], a[start + i]
        i += 1
        times = times - 1
    return a

b = reverseArr([1, 2, 3, 4 ,5], 0, 1)
print(b)