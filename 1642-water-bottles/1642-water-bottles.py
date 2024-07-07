class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed = 0    # count the drinked bottles
        while(numBottles >= numExchange):
            # consumed bottle exchange with new filled bottle
            consumed += numExchange
            # decrement of of numbottle with exchange bottle
            numBottles -= numExchange
            # by taking new filled bottle through the exchange
            numBottles += 1
        # return the total consumed and numbottles
        return consumed+numBottles