class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # intialize two empty arrays
        arr1, arr2 = [], []
        
        lenght = len(nums)
        # iterate on nums and append all the elements to both arrays
        for i in range(lenght):
            arr1.append(nums[i])
            arr2.append(nums[i])
        # concatenate the both arrays
        ans = arr1 + arr2
        
        return ans