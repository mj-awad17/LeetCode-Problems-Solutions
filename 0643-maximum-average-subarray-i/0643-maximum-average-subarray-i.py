class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # calculate the sum of the first 'k' elements
        maxSum = windowSum = sum(nums[0:k])
        for i in range(len(nums)-k): 
            # Update the window
            # removing the first element of the previous window
            windowSum = windowSum + nums[i+k] - nums[i]
            maxSum = max(maxSum, windowSum)
            
        return maxSum/float(k)