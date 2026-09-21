class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_leave = False


## 字典树
class PrefixTree:

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode(ch)
            cur = cur.children[ch]
        cur.is_leave = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.is_leave

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True