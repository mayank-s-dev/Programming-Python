def isPalindrome(S):
    # code here
    str_len = len(S)
    mid = 1
    if str_len % 2 == 0:
        mid = int(str_len / 2)
    else:
        mid = int((str_len + 1) / 2)

    for i in range(0, mid):
        if S[i] != S[str_len - i - 1]:
            return 0

    return 1


s = isPalindrome("abba")

print(s)