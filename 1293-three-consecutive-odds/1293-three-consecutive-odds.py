class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # iterate the array
        for i in range(len(arr) - 2):
            # 
            if (arr[i] % 2 != 0) and (arr[i+1] % 2 != 0) and (arr[i+2] % 2 != 0):
                return True
        return False
        
        """# Sliding window approache
        n = len(arr)
        if n < 3:
            return False

        window = [arr[0], arr[1], arr[2]]
        if all(num % 2 != 0 for num in window):
            return True

        for i in range(3, n):
            window.pop(0)
            window.append(arr[i])
            if all(num % 2 != 0 for num in window):
                return True

        return False"""