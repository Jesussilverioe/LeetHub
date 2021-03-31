class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return None
        row = len(grid)
        col = len(grid[0])
        visited = set()
        island = 0
        def bfs(i,j):
            q = collections.deque()
            q.append((i,j))
            
            neigbors = [[1,0],[-1,0],[0,1],[0,-1]]
            visited.add((i,j))
            while q:
                point1,point2 = q.popleft()
                for nr,nc in neigbors:
                    np1 = point1 + nr
                    np2 = point2 + nc
                    if (0 <= np1 < row and 0 <= np2 < col and grid[np1][np2] == "1" and (np1,np2) not in visited):
                        q.append((np1,np2))
                        visited.add((np1,np2))
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    island += 1
                    
        return island