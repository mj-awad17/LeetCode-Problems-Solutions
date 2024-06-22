class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            num = abs(nums[i])
            # Ensure that num-1 is a valid index
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        return [i + 1 for i in range(n) if nums[i] > 0]