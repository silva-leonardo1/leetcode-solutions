class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        x = sorted(intervals, key=lambda y: y[0])
        final = [x[0][0]]
        index = x[0][1]

        for i in range(1, len(x)):
            if index == x[i][0] and index < x[i][1]:
                index = x[i][1]
            elif index < x[i][0]:
                final.append(index)
                final.append(x[i][0])
                index = x[i][1]
            elif index < x[i][1]:
                index = x[i][1]

        final.append(index)
        return [[final[i], final[i + 1]] for i in range(0, len(final), 2)]