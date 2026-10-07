class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            row_seen = set()
            col_seen = set()
            for j in range(9):
                #i=j=0: loop: checks 0,0 
                #then i=0, j=1: checks 0,1 and 1,0
                #until 0,8 and 8,0
                #first row and col complete
                
                if board[i][j].isnumeric():
                    if board[i][j] in row_seen:
                        return False
                    row_seen.add(board[i][j])
                
                if board[j][i].isnumeric():
                    if board[j][i] in col_seen:
                        return False
                    col_seen.add(board[j][i])

            #then i=1, j=0:
            #checks 2nd row and 2nd col

        #now check quads:
        #get starting coords
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                box_seen = set()
                #use starting coords to check box
                for i in range(3):
                    for j in range(3):
                        if board[box_row+i][box_col+j].isnumeric():
                            if board[box_row+i][box_col+j] in box_seen:
                                return False
                            box_seen.add(board[box_row+i][box_col+j])
                    
        return True