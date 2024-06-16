class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        maxreach = 0 #maximum reach number `current = 0`
        patch = 0 # patch number currently 0
        i = 0 # nums[i] i is number
        while maxreach < n:
            
            if nums[i] <= maxreach + 1:
                maxreach += nums[i]
                i += 1
            else:
                maxreach += maxreach+1
                patch += 1
        return patch
