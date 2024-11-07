class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_count = 0
        for bit in range(32):  # Check each bit position from 0 to 31
            count = 0
            for num in candidates:
                if num & (1 << bit):  # Check if the bit is set in num
                    count += 1
            max_count = max(max_count, count)
        return max_count