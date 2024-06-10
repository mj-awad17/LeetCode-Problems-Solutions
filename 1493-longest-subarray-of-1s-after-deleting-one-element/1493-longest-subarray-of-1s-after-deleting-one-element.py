class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxlen, i, count= 0, 0, 0

        for j in range(len(nums)):
        
            if nums[j] == 0:
                count += 1
        
            while count > 1:
                if nums[i] == 0:
                    count -= 1
        
                i += 1
            maxlen = max(maxlen, j-i)
        
        return maxlen