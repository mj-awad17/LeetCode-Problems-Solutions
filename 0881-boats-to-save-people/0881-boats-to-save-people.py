class Solution(object):
    def numRescueBoats(self, people, limit):
        arr = people
        target = limit
        arr.sort()
        i = 0
        j = len(arr)-1
        count = 0
        while(i <= j):
            if arr[i] + arr[j] <= target:
                count +=1
                i +=1
                j -=1
            else:
                count +=1
                j -= 1
        return count