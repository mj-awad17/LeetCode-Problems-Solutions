class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """# Create a frequency of nums1
        freq = {}
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1
        
        # traverse nums2 and find common elements 
        result = []
        for i in nums2:
            if i in freq and freq[i] >0:
                result.append(i)
                freq[num] -= 1
        return result"""

        # Create a frequency map for nums1
        freq_map = {}
        for num in nums1:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Traverse nums2 and find the common elements
        result = []
        for num in nums2:
            if num in freq_map and freq_map[num] > 0:
                result.append(num)
                freq_map[num] -= 1

        return result