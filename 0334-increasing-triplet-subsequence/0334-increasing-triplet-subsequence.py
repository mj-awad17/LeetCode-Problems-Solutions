class Solution(object):
    def increasingTriplet(self, nums):
        _1st = ('inf')
        _2nd = ('inf')
        for num in nums:
            if num <= _1st:
                _1st = num
            elif num <= _2nd:
                _2nd = num
            else:
                return True
        return False