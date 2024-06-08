class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursive Approach:
        # if n <= 2:
        #     return n
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # there is an issue with this code that time complexity is high so 'time limited exceed' error occur


        # Tabulation (Bottom-up Dynamic Programming):
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


        # Fibonacci Series (Optimal)
        # if n <= 2:
        #     return n
        # a, b = 1, 2
        # for i in range(3, n + 1):
        #     a, b = b, a + b
        # return b

        # Memoization (Top-down Dynamic Programming):
    #     memo = {}
    #     return self.helper(n, memo)

    # def helper(self, n: int, memo: dict) -> int:
    #     if n <= 2:
    #         return n
    #     if n in memo:
    #         return memo[n]
    #     memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
    #     return memo[n]