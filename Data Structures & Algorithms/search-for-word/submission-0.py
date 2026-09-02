class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited = []
        def dfs(r, c, i):
            if i >= len(word):
                return True
            if r >= len(board) or c >= len(board[0]) or r < 0 or c < 0 or [r, c] in self.visited:
                return False

            if word[i] != board[r][c] and i != 0:
                return False
            
            if word[i] == board[r][c]:
                self.visited.append([r, c])
                i += 1
            res = dfs(r + 1, c, i) or dfs(r - 1, c, i) or dfs(r, c + 1, i) or dfs(r, c - 1, i)
            if not res:
                self.visited.pop()
            return res
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    res = dfs(i, j, 0)
                    if res:
                        return True

        return False