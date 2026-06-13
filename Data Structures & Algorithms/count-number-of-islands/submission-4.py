class Solution:
    def dfs(self, grid, row, col):
        numrows = len(grid)
        numcols = len(grid[0])
        if (row < 0 or row >= numrows or col >= numcols or col < 0
        or grid[row][col] == '0'):
            return
        grid[row][col] = '0'
        self.dfs(grid, row+1, col)
        self.dfs(grid, row-1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count