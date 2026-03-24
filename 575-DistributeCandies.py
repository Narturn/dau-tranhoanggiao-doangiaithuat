class Solution(object):
    def distributeCandies(self, candyType):
        so_loai_keo = len(set(candyType))
        
        return min(so_loai_keo, len(candyType) / 2)