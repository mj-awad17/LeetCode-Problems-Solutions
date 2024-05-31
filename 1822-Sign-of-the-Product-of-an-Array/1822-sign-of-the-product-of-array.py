"""
Multiplication Approach

Intuition:
The idea behind this approach is to multiply all the elements in the input array nums and then check the sign of the result. 
If the product is positive, the function returns 1 (positive sign), if it's negative, the function returns -1 (negative sign),
and if it's zero, the function returns 0 (zero sign).

Complexity:

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution(object):
    def arraySign(self, nums):
        p = 1
        for i in nums:
            p *= i 
        if p > 0:
            return 1
        elif p < 0:
            return -1
        else: 
            return 0
"""
Bitwise Approach

Intuition:
The idea behind this approach is to keep track of the sign of the product using a single variable sign. 
If any element is 0, the product will be 0, so the function can return 0 immediately. 
Otherwise, the function updates the sign variable based on the sign of the current element.

Complexity:

Time Complexity: O(n)
Space Complexity: O(1)

"""
class Solution(object):
    def arraySign(self, nums):
        sign = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                sign *= -1
        return sign
