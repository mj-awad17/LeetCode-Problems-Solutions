class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #1 initial max = -1
        #2 reverse iteration
        #3 newMax = max(oldMax, arr[i])
        
        right_max = -1
        for i in range(len(arr) -1, -1, -1):
            newMax = max(right_max, arr[i])
            # swap the ith element of array with right_max variable
            arr[i] = right_max
            right_max = newMax
        return arr