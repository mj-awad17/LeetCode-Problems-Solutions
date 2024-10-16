class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # max window initial
        max_w = 0
        # counts zeros
        nums_zeros = 0
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] == 0:
                nums_zeros += 1
                # conditionla on the total counts zeros to given k
            while nums_zeros > k:
                if nums[l] == 0:
                    nums_zeros -= 1
                l += 1
            # window sizing 
            w = r - l + 1
            max_w = max(max_w, w)
        return max_w