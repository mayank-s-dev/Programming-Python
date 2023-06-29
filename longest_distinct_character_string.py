def longestSubstrDistinctChars(S):
    longest = 1
    curr_longest = 0
    dict = {}
    i = 0
    while i < len(S):
        if dict.get(S[i]) is None:
            curr_longest += 1
            dict[S[i]] = i
            i += 1
        else:
            longest = max(curr_longest, longest)
            i = dict[S[i]] + 1
            dict = {}
            curr_longest = 0


    print(longest)
    return longest

longestSubstrDistinctChars("qwertyuioplkjh")