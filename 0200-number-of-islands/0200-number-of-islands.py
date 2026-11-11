from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        
        rows = len(grid)
        columns = len(grid[0])
        islands = 0

        for row in range(rows):
            for col in range(columns):
                cell = grid[row][col]
                coord = (row, col)
                if cell == "1" and coord not in visited:
                    dq = deque([(row, col)])
                    visited.add(coord)
                    islands += 1

                    while dq:
                        r, c = dq.popleft()
                        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                            if (0 <= nr < rows and 0 <= nc < columns) and (nr, nc) not in visited and grid[nr][nc] == "1":
                                dq.append((nr, nc))
                                visited.add((nr, nc))
        return islands
 







