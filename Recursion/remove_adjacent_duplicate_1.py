class Solution:
    def rremove(self, S):
        # code here
        store = S
        match = False
        count = 1
        n = len(S)
        i = 1
        while i < n:
            if S[i] == S[i - 1]:
                count += 1
                # print(S[i], count)
            else:
                if count > 1:
                    # print("1", S)
                    S = S.replace(S[i - count:i], "")
                    i = i - count + 1
                    n = len(S)

                count = 1

            i += 1

        if count > 1:
            S = S.replace(S[i - count:i], "")

        # print(store, S)
        if store == S:
            return store

        return self.rremove(S)


res = Solution().rremove("offevqqszsaksjyyyiirrdddwwddbbhwwyyjjivwaaxdmhuumssszxxeeeuuqppaliirrfddn")
print(res)
