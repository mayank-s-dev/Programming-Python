def isSubSequence(A, B):
    # code here

    i = 0
    j = 0
    str_b = len(B)
    str_a = len(A)

    if str_a > str_b:
        return False

    while i < str_a and j < str_b:
        print(A[i], B[j])
        if A[i] == B[j]:
            j += 1
            i += 1
            print("j", j)
            if i == len(A):
                return True
        else:
            j += 1

    return False

res= isSubSequence("RATAT", "KARAATTAT")
print(res)