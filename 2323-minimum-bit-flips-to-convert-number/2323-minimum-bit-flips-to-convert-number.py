class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # method 1
        """res = 0
        while start or goal:
            if (start % 2) != (goal % 2):
                res += 1
            start =  start >> 1
            goal  =  goal >> 1
        return res"""
        # method 2 - XOR
        """res = 0
        n = start ^ goal
        while n:
            res += n & 1
            n = n >> 1
        return res"""
        # method 3 - Brain Keringhar'a Algorithm
        res = 0
        n = start ^ goal
        while n:
            n = n & (n-1)
            res += 1
        return res