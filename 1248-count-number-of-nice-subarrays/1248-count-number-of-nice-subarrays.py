class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        oddcount, preCount, result, i, j = 0, 0, 0, 0, 0
        while (j < n):
            if nums[j] % 2 != 0:
                oddcount += 1
                preCount = 0
            while(oddcount == k):
                preCount += 1
                if (nums[i] % 2 == 1):
                    oddcount -= 1
                i += 1
            result += preCount
            j += 1
        return result