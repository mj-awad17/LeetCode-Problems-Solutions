class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = [-1]
        set_arr = set(arr)
        for i in set_arr:
            if arr.count(i)==i:
                ans.append(i)
        excute = max(ans)
        return excute