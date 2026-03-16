class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        result = 0
        bottles = 0

        while numBottles > 0:
            result += numBottles
            bottles += numBottles
            numBottles = bottles / numExchange
            bottles %= numExchange
        
        return result