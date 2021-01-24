# Find the min no. of coins to make up an amount
class Solution:
    def coinChange(self, coins, amount):
        dp = [
            99 for i in range(amount + 1)
        ]  # each pos represents min coins for that amount
        dp[0] = 0
        for i in range(1, amount + 1):
            for amt in coins:
                if amt <= i:
                    dp[i] = min(dp[i], dp[i - amt] + 1)
        if dp[amount] == 99:
            return -1
        return dp[amount]
