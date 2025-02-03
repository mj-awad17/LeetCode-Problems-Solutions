class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array to minimize the binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # Ensures the left partition has enough elements for median calculation

        low, high = 0, m

        while low <= high:
            i = (low + high) // 2  # Partition point in nums1
            j = half - i           # Corresponding partition point in nums2

            # Handle edge cases where partitions are at the boundaries
            max_left_A = nums1[i-1] if i > 0 else float('-inf')
            min_right_A = nums1[i] if i < m else float('inf')
            max_left_B = nums2[j-1] if j > 0 else float('-inf')
            min_right_B = nums2[j] if j < n else float('inf')

            # Check if the current partitions are valid
            if max_left_A <= min_right_B and max_left_B <= min_right_A:
                # Calculate the median based on total number of elements
                if total % 2 == 1:
                    return max(max_left_A, max_left_B)
                else:
                    return (max(max_left_A, max_left_B) + min(min_right_A, min_right_B)) / 2
            elif max_left_A > min_right_B:
                # Adjust the partition to the left in nums1
                high = i - 1
            else:
                # Adjust the partition to the right in nums1
                low = i + 1
        return 0.0  # This return is a safeguard and theoretically unreachable