class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k

        # count the frequency of each remainder
        for number in arr:
            remainder = number % k
            # adjust remainder to non-negetive
            if remainder < 0:
                remainder += k
            remainder_count[remainder] += 1

        # check each remainder and its complement
        for r in range(1, (k//2)+1):
            if remainder_count[r] != remainder_count[k-r]:
                return False
            
        # check the special case for remainder 0
        if remainder_count[0] % 2 != 0:
            return False
        
        # Check the special case for k even
        if k % 2 == 0 and remainder_count[k // 2] % 2 != 0:
            return False
        
        return True