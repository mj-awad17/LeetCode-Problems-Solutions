class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # base case
        if n <= 0:
            return
        
        # check power of 2
        return (n & (n-1)) == 0