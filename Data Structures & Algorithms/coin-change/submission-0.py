class Solution:

    def helper(self, i, dp, amt, coins):

        INT_MAX = 199999999

        if amt == 0:
            return 0

        if amt < 0:
            return INT_MAX

        if i == len(coins):
            return INT_MAX

        if dp[i][amt] != -1:
            return dp[i][amt]

        not_take = self.helper(i + 1, dp, amt, coins)

        take = 1 + self.helper(i, dp, amt - coins[i], coins)

        dp[i][amt] = min(take, not_take)

        return dp[i][amt]

    def coinChange(self, coins: List[int], amount: int) -> int:

        INT_MAX = 199999999

        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        ans = self.helper(0, dp, amount, coins)

        if ans == INT_MAX:
            return -1
        else:
            return ans
