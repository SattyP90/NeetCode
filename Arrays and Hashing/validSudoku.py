class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9 #9 rows 1-9
        cols = [0] * 9
        squares = [0] * 9 

        for r in range(9): #9 columns 1-9
            for c in range(9): #9 rows 1-9
                if board[r][c] == ".": #if item in the cell is a . then continue 
                    continue
                
                val = int(board[r][c]) - 1 #convert the string to an integer and subtract 1 to get the index of the value
                if (1 << val) & rows[r]: #if the value is already in the row return False
                    return False
                if (1 << val) & cols[c]:#if the value is already in the column return False
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]: #if the value is already in the square return False
                    return False
                    
                rows[r] |= (1 << val) #add the value to the row
                cols[c] |= (1 << val)   #add the value to the column
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)   #add the value to the square

        return True     #return True if the board is valid