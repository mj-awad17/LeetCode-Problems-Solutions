class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Return 2^31 - 1 to avoid overflow

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Use absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        # Calculate the quotient using bit manipulation
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        # Apply the sign to the quotient
        if negative:
            quotient = -quotient

        # Ensure the quotient is within the 32-bit signed integer range
        return max(min(quotient, 2**31 - 1), -2**31)
