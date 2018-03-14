class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        
        col = len(board)
        row = 0
        sum = 0
        if col>0 :
            row =len(board[0])

        for i in range(col):
            for j in range(row):
                if 'X'== board[i][j]:
                    sum += 1
                    if  j+1 < row and  'X' == board[i][j+1]:
                        for k in range(j+1, row):
                            if 'X' == board[i][k]:
                                board[i][k]='.'
                            else:
                                break
                    if  i+1 < col and  'X' == board[i+1][j]:
                         for k in range(i+1, col):
                            if 'X' == board[k][j]:
                                board[k][j]='.'
                            else:
                                break

        return sum  
    #system
    def countBattleships1(self, board):
        if len(board) == 0: return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    count += 1
        return count  