class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        co = set()
        ro = set()
        blo = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    tempco = (j,board[i][j])
                    tempro = (i,board[i][j])
                    tempblo =(i//3,j//3,board[i][j])
                    if tempro in ro or tempco in co or tempblo in blo:
                        return False
                    ro.add(tempro)
                    co.add(tempco)
                    blo.add(tempblo)
        return True