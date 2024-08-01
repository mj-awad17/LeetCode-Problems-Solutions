class Solution:
    def maxProduct(self, nums: List[int]) -> int:
                #kandanes algorithm 
        #forward pass
        curr_prod = 1
        max_prod = float('-inf')
        for i in nums:
            curr_prod = i * curr_prod
            max_prod = max(max_prod, curr_prod)
            if curr_prod == 0:
                curr_prod = 1
        #reverse pass
        curr_prod = 1
        for i in range(len(nums)- 1, - 1 , -1) :  # (start, end, jump)
            curr_prod = nums[i] * curr_prod
            max_prod = max(max_prod, curr_prod)
            if curr_prod == 0:
                curr_prod = 1
        
        return max_prod