# User function Template for python3

def saveIronman(S):
    # Complete the function
    filtered_str = ""
    for i in range(0, len(S)):
        uni = ord(S[i])
        if (65 <= uni <= 90) or (97 <= uni <= 122):
            filtered_str += S[i].lower()

    i = 0
    print("aa", filtered_str)
    j = len(filtered_str) - 1
    while i < j:
        if filtered_str[i] != filtered_str[j]:
            return False

            i += 1
            j -= 1
        return True

saveIronman("bb211234")