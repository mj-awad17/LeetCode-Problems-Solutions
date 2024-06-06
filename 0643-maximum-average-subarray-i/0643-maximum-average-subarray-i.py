class Solution(object):
    def findMaxAverage(self, nums, k):
        maxSum = windowSum = sum(nums[0:k])
        for i in range(len(nums)-k): 
            windowSum = windowSum + nums[i+k] - nums[i]
            maxSum = max(maxSum, windowSum)
        return maxSum/float(k)