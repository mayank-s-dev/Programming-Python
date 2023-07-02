class Solution:
    def rremove(self, S):
        print(S)
        # code here
        l = list(S)
        n = len(l)

        left = 0
        right = 1

        match = False
        while left < n and right < n:
            if l[left] == l[right]:
                match = True
                right += 1
            else:
                if match:
                    for i in range(left, right):
                        l[i] = ""

                left = right
                right += 1
                match = False

        if match:
            for i in range(left, right):
                l[i] = ""

        S1 = "".join(l)
        # print(S1)
        if S1 == S:
            return S1

        return self.rremove(S1)


res = Solution().rremove("acaaabbbacdddd")
print(res)
