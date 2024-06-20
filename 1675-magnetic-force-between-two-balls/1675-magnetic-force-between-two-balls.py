class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # sort the given array
        position.sort()
        # take two pointer
        low, high = 1, (position[-1] - position[0]) // (m - 1)  
        answer = 1

        while low <= high:
            mid = low + (high - low) // 2

            if self.PlaceHere(position, mid, m):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return answer

    def PlaceHere(self, arr: List[int], dist: int, balls: int) -> bool:
        Balls_count = 1
        PlacedLast = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - PlacedLast >= dist:
                Balls_count += 1
                PlaceLast = arr[i]
            if Balls_count >= balls:
                return True
        return False