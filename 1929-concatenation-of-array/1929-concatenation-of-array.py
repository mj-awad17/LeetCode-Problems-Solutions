class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for i in range(len(nums)):
            arr1.append(nums[i])
            arr2.append(nums[i])
        ans = arr1 + arr2
        return ans