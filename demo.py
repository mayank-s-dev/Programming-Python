binary_str = "101"
strr = ""
for j in range(0, 2):
    for i in range(0, len(binary_str)):
        if binary_str[i] == '0':
            strr += "01"
        else:
            strr += "10"

    binary_str = strr
    strr = ""

print(binary_str)

