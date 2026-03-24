class Solution(object):
    def minimumCost(self, cost):
        pay = 0
        cost.sort()
        count = 0

        for i in range(len(cost) -1, -1, -1):
            count += 1
            if not count % 3 == 0:
                pay += cost[i]
            
        return pay