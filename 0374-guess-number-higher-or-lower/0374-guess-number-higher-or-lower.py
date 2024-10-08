class Solution:
    def guessNumber(self, n: int) -> int:
        # setting the range 1-n
        low, high = 1, n
        
        while low <= high:
            # midpoint of the current range
            mid = (low + high) // 2
            result = guess(mid)
            # condition states
            if result == 0:
                return mid
            elif result < 0:
                high = mid - 1
            else:
                low = mid + 1
        return -1