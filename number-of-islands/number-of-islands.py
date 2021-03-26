class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        island = 0
        visited = set()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    self.bfs(r,c,row,col,visited, grid)
                    island += 1
        return island
    
    def bfs(self, r,c,row,col,visited, grid):
        visited.add((r,c))
        q = collections.deque()
        q.append((r,c))
        while q:
            point1, point2 = q.popleft()
            neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
            for n,nc in neighbors:
                npoint1 = point1+n
                npoint2 = point2+nc
                if (npoint1 in range(row) and npoint2 in range(col) and grid[npoint1][npoint2] == "1"
                    and (npoint1, npoint2) not in visited):
                    visited.add((npoint1,npoint2))
                    q.append((npoint1,npoint2))
                    
        