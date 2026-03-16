class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        poison_time = 0
        
        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i+1] - timeSeries[i]
            if gap >= duration:
                poison_time += duration
            else:
                poison_time += gap
        
        return poison_time + duration