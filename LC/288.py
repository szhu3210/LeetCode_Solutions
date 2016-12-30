class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.d=collections.defaultdict(set)
        for word in dictionary:
            if len(word)>1: 
                self.d[word[0]+(str(len(word)-2) )+word[-1]].add(word)
            else:
                self.d[word].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        ab=word[0]+(str(len(word)-2) if len(word)-2 else '')+word[-1] if len(word)>1 else word
        return len(self.d[ab])==0 or (self.d[ab]==set([word]))


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")