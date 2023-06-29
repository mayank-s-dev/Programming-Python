def productExceptSelf(nums, n):
    # code here

    totalZero = 0
    totalProduct = 1
    for i in range(0, n):
        if nums[i] == 0:
            totalZero += 1
        else:
            totalProduct *= nums[i]

    print(totalZero)
    if totalZero > 1:
        return [0] * n
    elif totalZero == 1:
        print("Yaha aaya")
        productArr = [0] * n
        print(productArr)
        for i in range(0, n):
            if nums[i] == 0:
                productArr[i] = totalProduct

        return productArr

    productArr = [1] * n
    for i in range(0, n):
        if nums[i] == 0:
            productArr[i] = totalProduct
        else:
            productArr[i] = int(totalProduct / nums[i])

    return productArr

z = productExceptSelf([1, 0], 2)
print(z)