class Solution(object):
    def findDifference(self, nums1, nums2):
        res = []
        set1 = set(nums1)
        set2 = set(nums2)
        # diff = set1-set2
        res1,res2 = set1.difference(set2), set2.difference(set1)
        res.append(res1)
        res.append(res2)
        return res