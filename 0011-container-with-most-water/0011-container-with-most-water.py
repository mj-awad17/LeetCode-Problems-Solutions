class Solution:
    def maxArea(self, height):
        # initialize two pointer
        lp = 0
        rp = len(height) - 1
        # Initialize the result to track the maximum area
        res = 0
        while lp < rp:
            # width between the two pointers
            w = rp - lp
            # determine the min hight
            h = min(height[lp], height[rp])
            # area formula
            a = w * h
            res = max(res, a)
            if height[lp] < height[rp]:
                # move left pointer to right
                lp += 1
            else:
                # move right pointer to left
                rp -= 1
        return res