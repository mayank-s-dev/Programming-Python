def strstr(s, x):
    # code here

    len_s = len(s)
    len_x = len(x)
    for i in range(0, len_s - len_x + 1):
        if s[i] == x[0]:
            isPresent = True
            for j in range(0, len_x):
                if s[i + j] == x[j]:
                    continue
                else:
                    isPresent = False
                    break

            if isPresent:
                return i

    return -1

s = strstr("abcabcabcd", "abcd")
print("s", s)