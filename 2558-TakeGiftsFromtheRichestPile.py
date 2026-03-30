class Solution(object):
    def pickGifts(self, gifts, k):
        for i in range(k):
            max = -1
            viTri = -1

            for i in range(len(gifts)):
                if gifts[i] > max:
                    max = gifts[i]
                    viTri = i
            
            gifts[viTri] = int(math.sqrt(max))

        return sum(gifts)