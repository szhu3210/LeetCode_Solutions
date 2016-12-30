class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.d=collections.defaultdict(list)
        for i, word in enumerate(words):
            self.d[word].append(i)
            
    def shortest(self, word1, word2):
        l1 = self.d[word1]
        l2 = self.d[word2]
        i, j = 0, 0
        shortest = None
        while i < len(l1) and j < len(l2):
            shortest = min(shortest, abs(l1[i] - l2[j])) if shortest else abs(l1[i] - l2[j])
            if l1[i] > l2[j]:
                j += 1
            else:
                i += 1
        return shortest

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")