class Solution(object):
    def twoSum(self, nums, target):
        view = {}
        for i in range(len(nums)):
            y = target-nums[i]
            if y in view:
                return [view[y], i]
            else:
                view[nums[i]] = i
        