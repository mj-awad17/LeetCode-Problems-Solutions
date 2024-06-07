class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k]) # O(k)
        maxSum = windowSum 
        for i in range(len(nums)-k): # O(n-k)
            windowSum = windowSum + nums[i+k] - nums[i] # O(n-k)
            maxSum = max(maxSum, windowSum) # O(n-k)
        return maxSum/k 
        # time O(n-k)
        # space O(1)