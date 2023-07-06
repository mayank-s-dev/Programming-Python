def UncommonChars(A, B):
    # code here

    alphabetA = [0] * 26
    alphabetB = [0] * 26

    for i in A:
        uni = ord(i)
        position = uni - 97

        if alphabetA[position] == 0:
            alphabetA[position] = 1

    for i in B:
        uni = ord(i)
        position = uni - 97

        if alphabetB[position] == 0:
            alphabetB[position] = 1

    res = ''
    for i in range(0, 26):
        if alphabetA[i] == 1 and alphabetB[i] == 0:
            res += chr(i + 97)
        elif alphabetA[i] == 0 and alphabetB[i] == 1:
            res += chr(i + 97)

    print(res)
    return res

UncommonChars("geeksforgeeks", "geeksquiz")