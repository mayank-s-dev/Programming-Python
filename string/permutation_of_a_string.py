def permute(start, end, string, res):
    if start == len(string):
        res.append("".join(string))
        return res

    for i in range(start, end):
        string[start], string[i] = string[i], string[start]
        permute(start + 1, end, string, res)
        string[start], string[i] = string[i], string[start]


res = []
input = "ABCD"
permute(0, len(input), list(input), res)
print(res, len(res))

# above program may have redundant values to resolve that please use set instead of list in response
