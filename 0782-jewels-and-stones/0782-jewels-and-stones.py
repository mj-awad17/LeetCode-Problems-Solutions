class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # initalize a varibale to count
        jewel_in_stone = 0
        # loop in stones
        for jewel in stones:
            # jewel present in jewels
            if jewel in jewels:
                # increment in jewel_in_stone variable
                jewel_in_stone += 1
        return jewel_in_stone