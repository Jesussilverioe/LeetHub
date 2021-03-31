class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0: return False
        row = len(board)
        col = len(board[0])
        
        def bfs(i, j, word):
            if len(word) == 0:
                return True
            temp = board[i][j]
            board[i][j] = '$'
            neigbors = [[0,1],[0,-1],[1,0],[-1,0]]
            for n1, n2 in neigbors:
                ni = i+n1
                nj = j+n2
                if 0 <= ni < row and 0 <= nj < col and board[ni][nj] == word[0]:
                    if bfs(ni,nj,word[1:]):
                        return True
            board[i][j] = temp
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and bfs(i,j, word[1:]):
                    return True
        return False