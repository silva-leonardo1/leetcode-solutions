from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        exit_loop = False
        time_elapsed = 0
        dq = deque()
        fresh = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 2:
                    dq.append((row, column))
                elif grid[row][column] == 1:
                    fresh += 1
                   
        while dq and fresh > 0:
            for _ in range(len(dq)):
                r, c = dq.popleft()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        dq.append((nr, nc))

            time_elapsed += 1
        return time_elapsed if fresh == 0 else -1

