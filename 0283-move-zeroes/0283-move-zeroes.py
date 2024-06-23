class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # initial non-zero-position 0
        # iterate the array
        # swap the non-zero position element to zero position element
        
        # non_zero_position = 0
        # for i in range(len(nums)):
        #     if nums[non_zero_position] != 0:
        #         nums[non_zero_position] = nums[i]
        #         nums[i] = nums[non_zero_position]
        #         nums[non_zero_position] = nums[i]
        #     non_zero_position += 1
        # # Fill the remaining elements with 0
        # for i in range(non_zero_position, len(nums)):
        #     nums[i] = 0
        
        # Initialize a pointer to keep track of the next position to write a non-zero element
        write_pos = 0
        
        # Iterate through the list
        for read_pos in range(len(nums)):
            # If the current element is non-zero, write it to the write_pos
            if nums[read_pos] != 0:
                nums[write_pos] = nums[read_pos]
                write_pos += 1
        
        # Fill the remaining elements with 0
        while write_pos < len(nums):
            nums[write_pos] = 0
            write_pos += 1