def roundToNearest(N):
    # Complete the function
    n = len(N)
    res = []
    i = -1
    flag = False
    carry = 0
    while True:
        if abs(i) == n + 1:
            break

        if int(N[-1]) > 5 and not flag:
            res.append("0")
            carry = 1
            flag = True
        elif int(N[-1]) <= 5 and not flag:
            res.append("0")
            carry = 0
            flag = True
        else:
            temp = int(N[i]) + carry
            ele = temp % 10
            carry = temp // 10
            # print(N[i], carry)
            res.append(str(ele))

        i = i - 1

    # print(carry)
    if carry:
        res.append(str(carry))

    res.reverse()
    return "".join(res)


print(roundToNearest("991"))
