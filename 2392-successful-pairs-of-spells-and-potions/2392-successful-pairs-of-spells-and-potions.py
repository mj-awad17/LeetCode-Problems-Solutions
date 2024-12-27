class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions array
        potions.sort()
        n = len(spells)
        m = len(potions)
        result = [0] * n
        
        def binary_search(target):
            left, right = 0, m
            while left < right:
                mid = (left + right) // 2
                if potions[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left  # The index of the first element >= target
        
        for i in range(n):
            # Calculate the minimum potion strength needed
            min_potion = (success + spells[i] - 1) // spells[i]  # Ceiling division
            index = binary_search(min_potion)
            result[i] = m - index  # All potions from index to end are valid
        
        return result