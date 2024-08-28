class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, count = 0, 0
        ''
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                count += 1
                l += 1
        return count
        """left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left"""