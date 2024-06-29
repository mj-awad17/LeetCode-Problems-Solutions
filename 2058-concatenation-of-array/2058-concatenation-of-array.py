class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # create two empty arrays
        arr1 = []
        arr2 = []
        # iterate all element and append to both arrays
        for i in range(len(nums)):
            arr1.append(nums[i])
            arr2.append(nums[i])
        # concatenation
        ans = arr1 + arr2
        return ans