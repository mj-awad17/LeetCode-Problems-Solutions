class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()  # Step 1: Sort the array
        left, right = 0, len(nums) - 1
        operations = 0
        
        while left < right:  # Step 4: Continue until pointers meet
            current_sum = nums[left] + nums[right]
            
            if current_sum == k:  # Step 3: Found a pair
                operations += 1
                left += 1
                right -= 1
            elif current_sum < k:  # Sum is too small
                left += 1
            else:  # Sum is too large
                right -= 1
                
        return operations