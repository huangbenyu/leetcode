class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.search_word(board,word,i,j):
                    return True
        return False


    def search_word(self, board, word, i,j):
        wordlen = len(word)
        if wordlen == 0:
            return True
        if not self.isequal(board,word[0],i,j):
            return False
        tmp =board[i][j]
        board[i][j]= "#"
        ret = self.search_word(board,word[1:],i-1,j) or self.search_word(board,word[1:],i+1,j)\
        or self.search_word(board,word[1:],i,j-1) or self.search_word(board,word[1:],i,j+1)
        w = word[0]

        board[i][j]=tmp
        return ret

    def isequal (self, board, ch , i,j):
        if i<0 or i>= len(board):
            return False
        if j<0 or j>=len(board[i]):
            return False   
        return board[i][j] == ch   