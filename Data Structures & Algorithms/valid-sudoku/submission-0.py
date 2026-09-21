from collections import Counter
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def checkrepeat(lis):
            freq = Counter(lis)
            del freq["."]
            for i in freq:
                if freq[i] > 1:
                    return True
            return False
    

        for i in board:
            if checkrepeat(i):
                return False
        

        #now transpose for coloumns
        for i in range(9):
            if checkrepeat(j[i] for j in board):
                return False
        

        #now grid
        
        defgrid = ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)) 
        for i in range(0,7,3):
            for k in range(0,7,3):
                if checkrepeat([board[int(defgrid[j][0]) + i][int(defgrid[j][1]) + k] for j in range(9)]):
                    return False
        return True