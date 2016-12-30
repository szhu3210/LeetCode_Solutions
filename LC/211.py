class Trie(object):
    def __init__(self):
        self.nexts = collections.defaultdict(Trie)
        self.valid = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root=Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur=self.root
        for c in word:
            cur=cur.nexts[c]
        cur.valid=True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        cur=[self.root]
        for c in word:
            if c=='.':
                t=[]
                for x in cur:
                    for y in x.nexts:
                        t.append(x.nexts.get(y))
                cur=t
            else:
                cur=[x.nexts.get(c) for x in cur if x.nexts.get(c)]
            if not cur:
                return False
        return (True in [x.valid for x in cur])

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")