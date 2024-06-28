class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """sett = set(nums)
        if len(sett) == len(nums):
            return False
        return True"""

        # 2nd approach
        dict = {}
        for i in nums:
            if i in dict:
                return 1
            else:
                dict[i] = 1
        return 0