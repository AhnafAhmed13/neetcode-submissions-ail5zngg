class Node:
    def __init__(self):
        self.vals = dict() # end: None

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.vals:
                curr.vals[ch] = Node()
            curr = curr.vals[ch]
        curr.vals["end"] = None

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.vals: return False
            curr = curr.vals[ch]
        return "end" in curr.vals

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.vals: return False
            curr = curr.vals[ch]
        return True
        
        