class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for i in range(len(walls)):
            x = walls[i][0]
            y = walls[i][1]
            grid[x][y] = -1

        for i in range(len(guards)):
            x = guards[i][0]
            y = guards[i][1]
            grid[x][y] = -1
        
        count = (n*m) - len(walls) - len(guards)
        t = 0
        while t < len(guards):
            gx = guards[t][0]
            gy = guards[t][1]

            #horizontal, left
            for j in range(gy - 1, -1, -1):
                if grid[gx][j] == -1:
                    break
                if grid[gx][j] == 0:
                    grid[gx][j] = 1
                    count -= 1
            
            #horizontal, right
            for j in range(gy + 1, n, 1):
                if grid[gx][j] == -1:
                    break
                if grid[gx][j] == 0:
                    grid[gx][j] = 1
                    count -= 1
            
            #vertical, up
            for k in range(gx - 1, -1, -1):
                if grid[k][gy] == -1:
                    break
                if grid[k][gy] == 0:
                    grid[k][gy] = 1
                    count -= 1
            
            #vertical, down
            for k in range(gx + 1, m, 1):
                if grid[k][gy] == -1:
                    break
                if grid[k][gy] == 0:
                    grid[k][gy] = 1
                    count -= 1
            t+=1
        return count