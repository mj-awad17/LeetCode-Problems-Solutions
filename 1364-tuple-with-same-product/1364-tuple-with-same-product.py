class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = {}

        # Step 1: Count products
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if product in product_count:
                    product_count[product] += 1
                else:
                    product_count[product] = 1
        
        # Step 2: Calculate the number of valid tuples
        total_tuples = 0
        for count in product_count.values():
            if count > 1:
                total_tuples += count * (count - 1) * 4  # Each pair contributes 8 tuples, divided by 2 for the pairs
        
        return total_tuples
