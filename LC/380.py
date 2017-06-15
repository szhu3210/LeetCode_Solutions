class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {} # key - position in list
        self.l = [] # numbers

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # check if already exist in l
        if val in self.d:
            return False
        # append to l and add key to d
        index = len(self.l)
        self.l.append(val)
        self.d[val] = index
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # check if not in l
        if val not in self.d:
            return False
        # find index through d and get val, then move the last element to this index and update that key
        if self.d[val]==len(self.l)-1:
            self.d.pop(val)
            self.l.pop()
            return True
        index = self.d[val]
        last = self.l.pop()
        self.l[index] = last
        self.d[last] = index
        self.d.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        # pick a random index in [0:len(l)]
        return random.choice(self.l)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()