class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        """n = len(nums)
        oddcount, preCount, result, i, j = 0, 0, 0, 0, 0
        while (j < n):
            if nums[j] % 2 != 0:
                oddcount += 1
                preCount = 0
            while(oddcount == k):
                preCount += 1
                if (nums[i] % 2 == 1):
                    oddcount -= 1
                i += 1
            result += preCount
            j += 1
        return result"""

        """# Brute force O(n^2)
        n = len(nums)
        count = 0
        for i in range(n):
            odd_count = 0
            for j in range(i, n):
                if nums[j] % 2 == 1:
                    odd_count += 1
                if odd_count == k:
                    count += 1
                if odd_count > k:
                    break
        return count"""
        n = len(nums)  # Length of the input array
        oddcount = 0   # Number of odd numbers in the current subarray
        preCount = 0   # Number of subarrays with exactly k odd numbers ending at the current index
        result = 0     # Final result (number of subarrays with exactly k odd numbers)
        i = 0          # Left pointer of the sliding window
        j = 0          # Right pointer of the sliding window

        while (j < n):
            # If the current number is odd, increment the odd count
            if nums[j] % 2 != 0:
                oddcount += 1
                preCount = 0  # Reset the preCount when we encounter a new odd number
            
            # While the odd count is equal to k, increment the preCount
            # and update the odd count if the leftmost number is odd
            while(oddcount == k):
                preCount += 1
                if (nums[i] % 2 == 1):
                    oddcount -= 1
                i += 1
            
            # Add the preCount to the result
            result += preCount
            j += 1
        
        return result