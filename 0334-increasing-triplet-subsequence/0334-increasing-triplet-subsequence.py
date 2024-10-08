class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Initialize the 1st & 2nd smallest number to positive infinity
        _1st = ('inf')
        _2nd = ('inf')
        # iterate through list
        for num in nums:
            if num <= _1st:
                _1st = num
            elif num <= _2nd:
                _2nd = num
            else:
                return True
        return False
