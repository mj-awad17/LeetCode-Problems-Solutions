class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # base case
        if not nums:
            return 0


        max_length = 1
        inc_length = 1
        dec_length = 1

        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc_length += 1
                dec_length = 1  # reset
            elif nums[i] < nums[i - 1]:
                dec_length += 1
                inc_length = 1  # reset
            else:
                inc_length = 1  # reset
                dec_length = 1  # reset

            max_length = max(max_length, inc_length, dec_length)

        return max_length