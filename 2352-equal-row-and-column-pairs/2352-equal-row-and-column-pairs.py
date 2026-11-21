class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        cols = {}
        count = 0

        for i in range(len(grid[0])):
            temp = []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            cols[tuple(temp)] = cols.get(tuple(temp), 0) + 1
        print(cols)
        for row in grid:
            if tuple(row) in cols and cols[tuple(row)] > 0:
                count += cols[tuple(row)]
        
        return count