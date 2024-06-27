class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """# first edge
        u, v = edges[0]
        # first node present in second edge
        if u in [edges[1][0], edges[1][1]]:
            return u
        else:
            return v
        """

        # 2nd approach
        count = []
        for e in edges:
            if e[0] in count:
                return e[0]
            if e[1] in count:
                return e[1]
            count.append(e[0])
            count.append(e[1])