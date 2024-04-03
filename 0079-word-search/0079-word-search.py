class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        
        m, n, w = len(board), len(board[0]), len(word) - 1
        
        def dfs(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            if board[i][j] == '#':
                return False
            
            if k == w:
                return True
            
            tmp = board[i][j]
            board[i][j] = '#'
            
            k += 1
            
            for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if dfs(i + x, j + y, k):
                    return True
            
            board[i][j] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False