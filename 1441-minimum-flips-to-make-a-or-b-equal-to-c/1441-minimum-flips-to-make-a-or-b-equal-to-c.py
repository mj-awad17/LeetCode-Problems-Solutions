class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        # >> = right most shift, '&' and operator
        for i in range(32):  # Check each bit position
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1
            
            # Check if OR operator holds by -> (bit_a | bit_b) matches bit_c
            if (bit_a | bit_b) != bit_c:
                if bit_c == 1:
                    # If bit_c is 1, we need at least one of bit_a or bit_b to be 1
                    count += 1
                else:
                    # If bit_c is 0, both bits must be 0
                    count += bit_a + bit_b  # Count how many bits need to be flipped to 0

        return count