class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        size = len(flowerbed)
        i = 0
        while i < size:
            if flowerbed[i] == 0:
                if i == size - 1 or flowerbed[i+1] == 0:
                    count += 1
                    i += 2
                else:
                    i += 1
            else:
                i += 2
        return count >= n