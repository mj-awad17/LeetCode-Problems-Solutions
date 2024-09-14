class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Step 1: Find the maximum value in the array
        max_value = max(nums)
        
        # Step 2: Initialize two variables
        longest_length = 0
        current_length = 0
        
        # Step 3: Count the longest contiguous subarray with elements equal to max_value
        for num in nums:
            if num == max_value:
                current_length += 1
                longest_length = max(longest_length, current_length)
            else:
                current_length = 0
        
        return longest_length