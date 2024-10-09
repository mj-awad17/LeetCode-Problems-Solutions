class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        # finding the current maximum number of candy
        max_candies = max(candies)
        # storing the result
        result = []
        for c in candies:
        # Check if the current kid can have the greatest number of candies
        # after receiving the extra candies
            result.append(c + extraCandies >= max_candies)
        return result        