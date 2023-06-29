def reverseWords(S):
    # code here

    new_str = ''
    str_len = len(S)
    word = ''
    for i in range(str_len - 1, -1, -1):
        if S[i] != '.':
            word = S[i] + word
        else:
            new_str += word
            new_str += '.'
            word = ''

    new_str += word
    print(new_str)
    return new_str

reverseWords('i.like.this.program.very.much')