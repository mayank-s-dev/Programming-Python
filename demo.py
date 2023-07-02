class Solution(object):
    def removeDuplicates(self, s, k):
        size = len(s)
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            elif s[i] != s[i - 1]:
                count = 1

        if count == k:
            # found duplicates to remove
            s = s.replace(s[i - k + 1:i + 1], "")
            # backpropagation returned string
            return self.removeDuplicates(s, k)
        # loop exits, no duplicates, backpropagation this guy up the recursive stack

        return s