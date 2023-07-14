class Solution:
    def helper(self, coins, itr, sum):
        if itr < 0:
            return 0

        if sum == 0:
            return 1

        if sum < 0:
            return 0

        a = max(self.helper(coins, itr, sum - coins[itr]), self.helper(coins, itr - 1, sum - coins[itr]))
        return a + self.helper(coins, itr - 1, sum)

    def count(self, coins, N, Sum):
        # code here
        return self.helper(coins, N - 1, sum)

