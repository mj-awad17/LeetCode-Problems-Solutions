class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        # count the flowers that are placed
        count = 0
        size = len(flowerbed)
        i = 0
        while i < size:
            # the current spot is empty
            if flowerbed[i] == 0:
                # Check the last spot or the next spot is also empty
                if i == size - 1 or flowerbed[i+1] == 0:
                    count += 1
                    # move to next spot after one
                    i += 2
                else:
                    # move one sopt next
                    i += 1
            else:
                # skip if flowered ploted
                i += 2
        return count >= n