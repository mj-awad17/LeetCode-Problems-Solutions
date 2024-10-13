class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Count the occurrences of each element in the array
        count = Counter(arr)
        # Create a set to track unique frequencies
        occurrences = set()
        # Iterate through the counted frequencies
        for freq in count.values():
            # If the frequency is already in the set, occurrences are not unique
            if freq in occurrences:
                return False
            # Add the frequency to the set
            occurrences.add(freq)
        return True