final = [0, 2, 3, 0, 0]
_str = ""
f = len(final) - 1
fnz = False
print("f", f)
while f >= 0:
    print("loop", f, final[f], fnz)
    if final[f] == 0 and fnz:
        _str = _str + str(final[f])
    elif final[f] > 0:
        _str = _str + str(final[f])
        fnz = True

    f -= 1

print(_str)