class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                prev = flowerbed[i-1] if i > 0 else 0
                next = flowerbed[i+1] if i < len(flowerbed)-1 else 0
                if prev == 0 and next == 0:
                    flowerbed[i] = 1
                    count += 1
            if count >= n:
                return True
        return count >= n