class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d=collections.OrderedDict([])

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.d:
            return -1
        value = self.d.pop(key)
        self.d[key] = value
        return value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.d:
            self.d.pop(key)
        elif len(self.d) == self.capacity:
                self.d.popitem(last=False)
        self.d[key]=value
                
        