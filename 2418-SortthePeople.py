class Solution(object):
    def sortPeople(self, names, heights):
        arr = []
        result = []

        for i in range(len(names)):
            arr.append([heights[i], names[i]])

        arr.sort(reverse = True)

        for i in arr:
            result.append(i[1])

        return result