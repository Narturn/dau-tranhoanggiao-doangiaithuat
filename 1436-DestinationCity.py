class Solution(object):
    def destCity(self, paths):
        start_city = set()

        for i in paths:
            start_city.add(i[0])
        for i in paths:
            destination = i[1]
            if destination not in start_city:
                return destination