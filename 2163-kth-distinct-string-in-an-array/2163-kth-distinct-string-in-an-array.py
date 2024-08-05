class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = set()
        seen = set()
        for s in arr:
            if s in seen:
                distinct.discard(s)
            else:
                distinct.add(s)
                seen.add(s)
        
        for s in arr:
            if s in distinct:
                k -= 1
                if k == 0:
                    return s
        return ""
        """# App-2
        count = Counter(arr)
        for i in arr:
            if count[i] == 1:
                k -= 1
                if k == 0:
                    return i
        return ''"""