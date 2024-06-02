class Solution(object):
    def combine(self, n, k):
        ans = []
        def backtrack(start, combo):
            if len(combo) == k:
                ans.append(combo[:])
                return
            for i in range(start, n+1):
                combo.append(i)
                backtrack(i+1, combo)
                combo.pop()

        backtrack(1, [])
        return ans