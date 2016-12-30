class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nexts = collections.defaultdict(TrieNode)
        self.valid = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            cur=cur.nexts[c]
        cur.valid = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if not cur.nexts.get(c):
                return False
            cur = cur.nexts.get(c)
        return cur.valid

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if not cur.nexts.get(c):
                return False
            cur = cur.nexts.get(c)
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")