def multiplyStrings(self, s1, s2):
    # code here
    # return the product string
    _s2 = len(s2)
    _s1 = len(s1)
    if _s1 == 0 or _s2 == 0:
        return "0"

    sign = False
    if s1[0] == "-":
        s1 = s1[1:]
        _s1 -= 1
        sign = not sign

    if s2[0] == "-":
        s2 = s2[1:]
        _s2 -= 1
        sign = not sign

    final = [0] * (_s1 + _s2)
    for t in range(_s2 - 1, -1, -1):
        carry = 0
        i = _s2 - t - 1
        for o in range(_s1 - 1, -1, -1):
            temp_product = int(s2[t]) * int(s1[o]) + final[i] + carry
            ele = temp_product % 10
            carry = temp_product // 10
            final[i] = ele
            i += 1

        if carry > 0:
            final[i] += carry

    res_str = ""
    f = len(final) - 1
    fnz = False
    while f >= 0:
        if final[f] == 0 and fnz:
            res_str = res_str + str(final[f])
        elif final[f] > 0:
            res_str = res_str + str(final[f])
            fnz = True

        f -= 1

    if res_str == "":
        return "0"

    if sign:
        res_str = "-" + res_str

    return res_str
