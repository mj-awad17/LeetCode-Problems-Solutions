class Solution:
    def countBits(self, n: int) -> List[int]:
        # initilize the zeros
        dp = [0] * (n + 1)
        
        offset = 1
        # For i = 1: dp[1] = 1 + dp[0] = 1
        # For i = 2: dp[2] = 1 + dp[0] = 1 (update offset to 2)
        # For i = 3: dp[3] = 1 + dp[1] = 2
        # For i = 4: dp[4] = 1 + dp[0] = 1 (update offset to 4)
        # For i = 5: dp[5] = 1 + dp[1] = 2
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp