class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        # iterate until 'l' is less than 'r'.
        while l < r:
            # Calculate the sum
            sum_val = numbers[l] + numbers[r]
            # sum is greater than the target, decrement 'r'.
            if sum_val > target:
                r -= 1
            # sum is less than the target, increment 'l'.
            elif sum_val < target:
                l += 1
            # sum is equal to the target, return the indices [l+1, r+1].
            else:
                return [l + 1, r + 1]