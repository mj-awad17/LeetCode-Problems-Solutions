class Solution:
    def numTrees(self, n: int) -> int:
        # Create a dynamic programming table to store the number of unique BSTs for each value of n
        dp = [0] * (n + 1)
        
        # Base case: for n = 0 or 1, there is 1 unique BST
        dp[0] = 1
        dp[1] = 1
        
        # Compute the number of unique BSTs for each value of n
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]