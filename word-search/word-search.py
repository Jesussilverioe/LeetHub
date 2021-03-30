class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0: return False

        row = len(board)
        col = len(board[0])
        def explore(i,j, word):
            if len(word) == 0:
                return True
            temp = board[i][j]
            board[i][j] = '$'
            neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
            
            for x,y in neighbors:
                newi = i+x
                newj = j+y
                if 0 <= newi < row and 0 <= newj < col and board[newi][newj] == word[0]:
                    if explore(newi,newj, word[1:]):
                        return True
            board[i][j] = temp
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and explore(i,j, word[1:]):
                    return True
        return False