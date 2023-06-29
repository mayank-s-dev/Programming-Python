# User function Template for python3
import sys
sys.setrecursionlimit(10000)
class Solution:
    def add_pattern(self, N, res, data):
        res.append(N)

        if N == data[1] and data[0]:
            return

        if N > 0 and not data[0]:
            N -= 5
        else:
            data[0] = True
            N += 5

        self.add_pattern(N, res, data)

    def pattern(self, N):
        # code here
        res = []
        data = [False, N]
        self.add_pattern(N, res, data)
        return res


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':


    ob = Solution()
    ans = ob.pattern(2501)
    print(ans)
# } Driver Code Ends