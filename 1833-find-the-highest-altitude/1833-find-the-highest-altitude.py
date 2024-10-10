class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Initialize the maximum altitude and current altitude
        maxAltitude = 0
        currAltitude = 0
        # Iterate through each gain value in the list
        for g in gain:
            # the current altitude by adding the current gain
            currAltitude += g
            # Update the maximum altitude if the current altitude is greater
            maxAltitude = max(maxAltitude, currAltitude)

        return maxAltitude
