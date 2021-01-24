class Solution:
    def change(self, amount, coins):
        # dp[i][j] represents the number of ways to get sum 'j' using the first 'i' coins
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    dp[i] += dp[i - coin]
        return dp[amount]
