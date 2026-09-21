class TrieNode:
    def __init__(self): 
        self.children = [None] * 26 
        self.idx = -1 
        self.refs = 0

    def add_word(self, word, idx):
        cur = self
        self.refs += 1
        for ch in word:
            i = ord(ch) - ord('a')
            if not cur.children[i]:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
            cur.refs += 1
        cur.idx = idx
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        res = []
        for i in range(len(words)):
            root.add_word(words[i], i)
        ROWS, COLS = len(board), len(board[0])
        def get_index(ch):
            return ord(ch) - ord('a')
        
        def dfs(r, c, node : TrieNode):
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS 
                or board[r][c] == "*" 
                or not node.children[get_index(board[r][c])]):
                return 0

            tmp = board[r][c]
            board[r][c] = "*"

            prev = node
            node = node.children[get_index(tmp)]

            found = 0
            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                found += 1

            found += dfs(r + 1, c,  node)
            found += dfs(r - 1, c, node)
            found += dfs(r, c + 1, node)
            found += dfs(r, c - 1, node)

            board[r][c] = tmp
            node.refs -= found

            if not node.refs:
                prev.children[get_index(tmp)] = None

            return found

        for r in range(ROWS):
            for c in range(COLS):
                root.refs -= dfs(r, c, root)

        return res


        