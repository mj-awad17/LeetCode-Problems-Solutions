"""
1 - Approach:

The approach used in this solution is as follows:
1. Sort the input arrays nums1 and nums2 in ascending order using the sort() method.
2. Access the first elements of the sorted arrays, which will be the minimum elements, using the index 0.
3. Calculate the difference between the minimum elements of nums2 and nums1, which will be the integer x that was added to nums1.
4. Return the calculated difference.

Complexity Analysis:
- Time Complexity: O(n log n)
- Space Complexity: O(1)
"""
class Solution(object):
    def addedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        return nums2[0] - nums1[0]
