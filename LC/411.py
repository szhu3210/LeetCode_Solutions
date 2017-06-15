class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        def checkWord(word, dictionary, l):
            # return if a word in valid according to the dictionary
            for check_word in dictionary:
                if l!=len(check_word):
                    continue
                i=0
                for element in abbr_word:
                    if type(element)==int: # a number indicates some str, just skip.
                        i += element
                    else:
                        if element != check_word[i]:
                            break # not match, continue to the next check_word
                        i += 1
                if i==l:
                    return False # match! not valid!
            return True # valid
        
        # 0. filter the dictionary
        l = len(target)
        dictionary = [d for d in dictionary if len(d)==l]
        if not dictionary: return str(l)
        
        # 1. list all the abbreviations
        abbr = [] # store all the abbr.
        for i in range(2**l):
            # bin(i) denotes an abbr.
            t = bin(i)[2:].zfill(l) # abbr in string format
            j = 0
            abbr_word = [] # a formatted abbr.
            while j<l:
                if t[j]=='1': # abbr starts here at j
                    k = j+1
                    while k<l and t[k]=='1':
                        k += 1
                    n = k-j # length of abbreviated chunk of string
                    abbr_word.append(n)
                    j = k
                else:
                    abbr_word.append(target[j])
                    j += 1
            abbr.append(abbr_word)
        
        # 2. sort the list
        abbr = sorted(abbr, key=len)
        
        # 3. iterate through the elements of the list and check, if valid abbr. found, return instantly.
        for abbr_word in abbr:
            if checkWord(abbr_word, dictionary, l):
                return ''.join(map(lambda x: str(x), abbr_word))