class Solution(object):
    def duplicateZeros(self, arr):
        note = []

        for i in arr:
            if i == 0:
                note.append(0)
                note.append(0)
            else:
                note.append(i)
        for i in range(len(arr)):
            arr[i] = note[i]