"""
2 - Approach:
The approach used in this solution is as follows:

1. Find the minimum element in nums1 using the min() function.
2. Find the minimum element in nums2 using the min() function.
3. Calculate the difference between the minimum elements of nums1 and nums2, which will be the integer x that was added to nums1.
4. Return the calculated difference.

Complexity Analysis:
- Time Complexity: O(n), 
- Space Complexity: O(1)
"""
class Solution(object):
    def addedInteger(self, nums1, nums2):
        return min(nums2) - min(nums1)