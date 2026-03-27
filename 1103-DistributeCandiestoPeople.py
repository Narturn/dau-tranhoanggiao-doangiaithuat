class Solution(object):
    def distributeCandies(self, candies, num_people):
        result = [0] * num_people
        count = 0
        give = 1

        while candies > 0:
            if count < candies:
                result[count % num_people] += give
            else:
                result[count % num_people] += candies
            
            candies -= give
            count += 1
            give += 1
        
        return result