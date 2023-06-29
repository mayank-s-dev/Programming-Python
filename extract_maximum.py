def extractMaximum(S):
    # code here
    max_num = -1
    num_str = ""
    for i in S:
        if i.isdigit():
            num_str += i
        else:
            if len(num_str) > 0:
                max_num = max(max_num, int(num_str))
                num_str = ""

    if len(num_str) > 0:
        max_num = max(max_num, int(num_str))

    print(max_num)
    return max_num

extractMaximum("1000000")